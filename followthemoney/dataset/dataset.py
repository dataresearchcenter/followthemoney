from datetime import datetime
from functools import cached_property
import logging
from typing import TYPE_CHECKING
from typing import Any, Dict, List, Optional, Set, Type, TypeVar

from pydantic import HttpUrl, field_validator, model_validator
from typing_extensions import Self
import yaml

from followthemoney.dataset.coverage import DataCoverage
from followthemoney.dataset.publisher import DataPublisher
from followthemoney.dataset.resource import DataResource
from followthemoney.dataset.util import (
    Named,
    OperationalBase,
    SerializableModel,
    dataset_name_check,
)
from followthemoney.exc import MetadataException
from followthemoney.util import PathLike
from followthemoney.value import string_list

if TYPE_CHECKING:
    from followthemoney.dataset.catalog import DataCatalog

DS = TypeVar("DS", bound="Dataset")
log = logging.getLogger(__name__)


class DatasetModel(SerializableModel):
    name: str
    title: str
    license: Optional[HttpUrl] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    url: Optional[HttpUrl] = None
    updated_at: Optional[datetime] = None
    last_export: Optional[datetime] = None
    entity_count: Optional[int] = None
    thing_count: Optional[int] = None
    version: Optional[str] = None
    category: Optional[str] = None
    tags: List[str] = []
    publisher: DataPublisher | None = None
    coverage: DataCoverage | None = None
    resources: List[DataResource] = []
    children: Set[str] = set()

    @field_validator("name", mode="after")
    @classmethod
    def check_name(cls, value: str) -> str:
        return dataset_name_check(value)

    @model_validator(mode="before")
    @classmethod
    def ensure_data(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if "name" not in data:
                raise MetadataException("Missing dataset name")
            data["title"] = data.get("title", data["name"])
            children = set(
                [
                    *data.get("children", []),
                    *data.get("datasets", []),
                    *data.get("scopes", []),
                ]
            )
            data["children"] = children
        return data

    def get_resource(self, name: str) -> DataResource:
        for res in self.resources:
            if res.name == name:
                return res
        raise ValueError("No resource named %r!" % name)


class Dataset(Named, OperationalBase):
    """A container for entities, often from one source or related to one topic.
    A dataset is a set of data, sez W3C."""

    Model = DatasetModel
    model: DatasetModel

    def __init__(
        self: Self,
        data: Dict[str, Any],
        model: Optional[Type[DatasetModel]] = DatasetModel,
    ) -> None:
        name = dataset_name_check(data.get("name"))
        super().__init__(name)

        self._children = set(string_list(data.get("children", [])))
        self._children.update(string_list(data.get("datasets", [])))
        self.children: Set[Self] = set()

        self.Model = model or DatasetModel
        self.model = self.Model(**data)

    @cached_property
    def is_collection(self: Self) -> bool:
        return len(self._children) > 0

    @property
    def datasets(self: Self) -> Set[Self]:
        current: Set[Self] = set([self])
        for child in self.children:
            current.update(child.datasets)
        return current

    @property
    def dataset_names(self: Self) -> List[str]:
        return [d.name for d in self.datasets]

    @property
    def leaves(self: Self) -> Set[Self]:
        """All contained datasets which are not collections (can be 'self')."""
        return set([d for d in self.datasets if not d.is_collection])

    @property
    def leaf_names(self: Self) -> Set[str]:
        return {d.name for d in self.leaves}

    def __hash__(self) -> int:
        return hash(repr(self))

    def __repr__(self) -> str:
        return f"<Dataset({self.name})>"  # pragma: no cover

    def get_resource(self, name: str) -> DataResource:
        return self.model.get_resource(name)

    @classmethod
    def from_path(
        cls: Type[DS], path: PathLike, catalog: Optional["DataCatalog[DS]"] = None
    ) -> DS:
        from followthemoney.dataset.catalog import DataCatalog

        with open(path, "r") as fh:
            data = yaml.safe_load(fh)
            if catalog is None:
                catalog = DataCatalog(cls, {})
            return catalog.make_dataset(data)

    @classmethod
    def make(cls: Type[DS], data: Dict[str, Any]) -> DS:
        from followthemoney.dataset.catalog import DataCatalog

        catalog = DataCatalog(cls, {})
        return catalog.make_dataset(data)

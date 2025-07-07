from typing import List, Literal, Optional, TypeAlias

from pydantic import field_validator

from followthemoney.dataset.util import PartialDate, SerializableModel, type_require
from followthemoney.types import registry


# Derived from Aleph
FREQUENCIES: TypeAlias = Literal[
    "unknown",
    "never",
    "hourly",
    "daily",
    "weekly",
    "monthly",
    "annually",
]


class DataCoverage(SerializableModel):
    """Details on the temporal and geographic scope of a dataset."""

    start: Optional[PartialDate] = None
    end: Optional[PartialDate] = None
    countries: List[str] = []
    frequency: FREQUENCIES = "unknown"
    schedule: Optional[str] = None

    @field_validator("countries", mode="after")
    @classmethod
    def ensure_countries(cls, value: List[str]) -> List[str]:
        return [type_require(registry.country, c) for c in value]

    def __repr__(self) -> str:
        return f"<DataCoverage({self.start!r}, {self.end!r}, {self.countries!r})>"

from typing import Optional

from pydantic import HttpUrl, field_validator

from followthemoney.dataset.util import SerializableModel, type_require
from followthemoney.types import registry


class DataPublisher(SerializableModel):
    """Publisher information, eg. the government authority."""

    name: str
    url: Optional[HttpUrl] = None
    name_en: Optional[str] = None
    acronym: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None
    official: Optional[bool] = False
    logo_url: Optional[HttpUrl] = None

    @field_validator("country", mode="after")
    @classmethod
    def ensure_country(cls, value: str) -> str:
        return type_require(registry.country, value)

    @property
    def country_label(self) -> Optional[str]:
        if self.country is None:
            return None
        return registry.country.caption(self.country)

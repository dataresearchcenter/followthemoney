import re
from typing import Optional, TYPE_CHECKING
from normality import slugify
from normality.cleaning import collapse_spaces
from rigour.addresses import normalize_address
from rigour.text.distance import levenshtein_similarity

from followthemoney.types.common import PropertyType
from followthemoney.util import defer as _
from followthemoney.util import dampen

if TYPE_CHECKING:
    from followthemoney.proxy import EntityProxy


class AddressType(PropertyType):
    """A geographic address used to describe a location of a residence or post
    box. There is no specified order for the sub-parts of an address (e.g. street,
    city, postal code), and we should consider introducing an Address schema type
    to retain fidelity in cases where address parts are specified."""

    LINE_BREAKS = re.compile(r"(\r\n|\n|<BR/>|<BR>|\t|ESQ\.,|ESQ,|;)")
    COMMATA = re.compile(r"(,\s?[,\.])")
    name = "address"
    group = "addresses"
    label = _("Address")
    plural = _("Addresses")
    matchable = True
    pivot = True

    def clean_text(
        self,
        text: str,
        fuzzy: bool = False,
        format: Optional[str] = None,
        proxy: Optional["EntityProxy"] = None,
    ) -> Optional[str]:
        """Basic clean-up."""
        address = self.LINE_BREAKS.sub(", ", text)
        address = self.COMMATA.sub(", ", address)
        collapsed = collapse_spaces(address)
        if collapsed is None or not len(collapsed):
            return None
        return collapsed

    def compare(self, left: str, right: str) -> float:
        left_norm = normalize_address(left)
        right_norm = normalize_address(right)
        if left_norm is None or right_norm is None:
            return 0.0
        return levenshtein_similarity(left_norm, right_norm, max_edits=3)

    def _specificity(self, value: str) -> float:
        return dampen(10, 60, value)

    def node_id(self, value: str) -> Optional[str]:
        slug = slugify(normalize_address(value))
        if slug is None:
            return None
        return f"addr:{value}"

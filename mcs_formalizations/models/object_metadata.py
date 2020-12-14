from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json

from mcs_formalizations._model import _Model


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class ObjectMetadata:
    """A model to parse data for a given object"""

    name: str
    long: float
    lat: float
    state_of_matter: str
    fillable: bool
    mixable: bool

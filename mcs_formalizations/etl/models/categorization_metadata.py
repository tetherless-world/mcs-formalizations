from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json

from mcs_formalizations.etl._model import _Model


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class CategorizationMetadata:
    """A model to parse metadata for a given categorization"""

    categorizer_name: str
    month_num: int
    day_num: int
    year_num: int

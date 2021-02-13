from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json

from typing import Tuple


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class CategorizationSample:
    """Data from a categorized question"""

    sample_question: str
    sample_labels: Tuple[str, ...]

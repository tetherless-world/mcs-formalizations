from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json
from typing import Dict

from typing import Tuple
from txt_classification.classifiers import Classifiers


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class ClassificationResults:
    """Results from a classifier"""

    classifier_type: Classifiers
    parameters: Dict
    file_name: str
    accuracy: float
    balanced_accuracy: float

import logging
from abc import abstractmethod
from typing import Generator
from pathlib import Path

from mcs_formalizations.etl._model import _Model
from mcs_formalizations.etl._pipeline_phase import _PipelinePhase


class _Transformer(_PipelinePhase):
    """
    Abstract base class for transformers.
    See the transform method.
    """

    @abstractmethod
    def transform(self, **kwds) -> Generator[_Model, None, None]:
        """
        Transform previously-extracted data into models.
        :param kwds: merged dictionary of initial extract kwds and the result of extract
        :return: generator of models
        """

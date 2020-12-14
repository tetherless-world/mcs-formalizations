import json
from abc import abstractmethod
from pathlib import Path
from rdflib import URIRef
from typing import Generator, Optional, Tuple, List, Dict

from mcs_formalizations._model import _Model
from mcs_formalizations._transformer import _Transformer
from mcs_formalizations.path import DATA_DIR_PATH

from mcs_formalizations.models.object_metadata import ObjectMetadata


class _ObjectTransformer(_Transformer):
    """
    Abstract base class for transformers.
    See the transform method.
    """

    @property
    def _uri_base(self):
        return URIRef(f"object:{self._pipeline_id}")

    def _generate_none(self) -> Generator[None, None, None]:
        while True:
            yield None

    def transform(
        self,
        **kwds,
    ) -> Generator[_Model, None, None]:

        object_json_file_path = (
            DATA_DIR_PATH / "metadata" / f"{self._pipeline_id}_metadata.json"
        )

        with open(object_json_file_path) as object_json:
            object_metadata = json.loads(object_json.read())

        object_bootstrap = ObjectMetadata.from_dict(object_metadata)

        yield from self._transform_object(object_bootstrap=object_bootstrap)

    @abstractmethod
    def _transform_object(
        self,
        *,
        object_bootstrap: Dict,
        **kwds,
    ) -> Generator[_Model, None, None]:
        """
        Transform previously-extracted data into models
        :return: generator of models
        """

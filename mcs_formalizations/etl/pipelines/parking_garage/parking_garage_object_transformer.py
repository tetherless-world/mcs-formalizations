import json
from pathlib import Path
from typing import Generator, Dict
from rdflib import URIRef

from mcs_formalizations._model import _Model
from mcs_formalizations._object_transformer import _ObjectTransformer
from mcs_formalizations.models.parking_garage import ParkingGarage
from mcs_formalizations.models.length_order import LengthOrder
from mcs_formalizations.models.weight_order import WeightOrder


class ParkingGarageObjectTransformer(_ObjectTransformer):
    def _transform_object(
        self,
        *,
        object_bootstrap: Dict,
        **kwds,
    ) -> Generator[_Model, None, None]:

        obj = ParkingGarage(
            uri=self._uri_base,
            name=object_bootstrap.name,
            lat=object_bootstrap.lat,
            long=object_bootstrap.long,
            state_of_matter=object_bootstrap.state_of_matter,
            fillable=object_bootstrap.fillable,
            mixable=object_bootstrap.mixable,
            is_full=False,
        )

        yield obj

        yield LengthOrder.kilometer(
            uri_base=self._uri_base,
            object_uri=obj.uri,
        )

        yield WeightOrder.kilotonne(uri_base=self._uri_base, object_uri=obj.uri)

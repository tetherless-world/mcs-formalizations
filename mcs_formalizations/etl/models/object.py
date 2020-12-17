from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json

from rdflib import Graph, Literal
from rdflib.resource import Resource
from mcs_formalizations.namespace import SCHEMA, GEO, XSD

from mcs_formalizations._model import _Model


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Object(_Model):
    """A physical object located in space"""

    name: str
    long: float
    lat: float
    state_of_matter: str
    fillable: bool
    mixable: bool

    def to_rdf(self, *, graph: Graph) -> Resource:
        resource = _Model.to_rdf(self, graph=graph)

        resource.add(SCHEMA.name, self._quote_rdf_literal(self.name))
        resource.add(GEO.long, Literal(self.long))
        resource.add(GEO.lat, Literal(self.lat))
        resource.add(XSD.string, self._quote_rdf_literal(self.state_of_matter))
        resource.add(XSD.boolean, Literal(self.fillable))
        resource.add(XSD.boolean, Literal(self.mixable))

        return resource

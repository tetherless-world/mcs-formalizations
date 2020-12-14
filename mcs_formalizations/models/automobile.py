from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json

from rdflib import Graph, Literal
from rdflib.resource import Resource

from mcs_formalizations.namespace import XSD

from mcs_formalizations.models.object import Object


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Automobile(Object):

    capacity: int

    def to_rdf(self, *, graph: Graph) -> Resource:
        resource = super().to_rdf(graph=graph)
        resource.add(XSD.integer, Literal(self.capacity))

        return resource

from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json

from rdflib import URIRef

from mcs_formalizations._model import _Model


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class WeightOrder(_Model):
    """The different orders of magnitude on which to measure weight on."""

    object_uri: URIRef

    @classmethod
    def gram(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":weight_order:1"),
            object_uri=object_uri,
        )

    @classmethod
    def centigram(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":weight_order:-2"),
            object_uri=object_uri,
        )

    @classmethod
    def kilogram(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":weight_order:3"),
            object_uri=object_uri,
        )

    @classmethod
    def tonne(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":weight_order:6"),
            object_uri=object_uri,
        )

    @classmethod
    def kilotonne(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":weight_order:9"),
            object_uri=object_uri,
        )

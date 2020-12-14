from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json

from rdflib import URIRef

from mcs_formalizations._model import _Model


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class LengthOrder(_Model):
    """The different orders of magnitude on which to measure length on."""

    object_uri: URIRef

    @classmethod
    def meter(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":length_order:1"),
            object_uri=object_uri,
        )

    @classmethod
    def centimeter(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":length_order:-2"),
            object_uri=object_uri,
        )

    @classmethod
    def kilometer(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":length_order:3"),
            object_uri=object_uri,
        )

    @classmethod
    def millimeter(cls, *, uri_base: str, object_uri: URIRef):
        return cls(
            uri=URIRef(uri_base + ":length_order:-3"),
            object_uri=object_uri,
        )

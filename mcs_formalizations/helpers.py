from rdflib import URIRef
from mcs_formalizations.namespace import MCS


def uri_base(obj_id):
    return URIRef("mcs:object:%s" % (obj_id))


def categories():
    return [
        "Time",
        "World states",
        "Events",
        "Space",
        "Physical Entities",
        "Values and quantities",
        "Classes and instances",
        "Sets",
    ]

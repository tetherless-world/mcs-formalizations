from rdflib import URIRef
from mcs_formalizations.namespace import MCS


def uri_base(obj_id):
    return URIRef("mcs:object:%s" % (obj_id))

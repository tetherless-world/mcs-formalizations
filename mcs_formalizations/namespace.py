from rdflib import Namespace, Graph

MCS = Namespace("http://purl.org/twc/mcs/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = Namespace("http://schema.org/")
VANN = Namespace("http://purl.org/vocab/vann#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
GEO = Namespace("http://www.w3.org/2003/01/geo#")


def bind_namespaces(g: Graph):
    g.bind("mcs", MCS)
    g.bind("owl", OWL)
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("schema", SCHEMA)
    g.bind("vann", VANN)
    g.bind("xsd", XSD)
    g.bind("geo", GEO)

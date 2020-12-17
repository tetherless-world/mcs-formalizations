from typing import Tuple

from rdflib import Graph
from rdflib.paths import Path

from mcs_formalizations.namespace import bind_namespaces
from mcs_formalizations.path import ROOT_DIR_PATH
from mcs_formalizations.reasoners._reasoner import _Reasoner


class SparqlReasoner(_Reasoner):
    def __init__(self):
        self.__graph = Graph()
        bind_namespaces(self.__graph)

    def add_knowledge(self, *triples):
        for triple in triples:
            self.__graph.add(triple)
        print("Graph after adding knowledge:")
        self.print_graph()

    def apply_rules(self, *rule_names: Tuple[str, ...]) -> None:
        # TODO: use a temporary Graph to store the inferred triples, so later rules don't match them?
        for rule_name in rule_names:
            with open(ROOT_DIR_PATH / "rules" / (rule_name + ".sparql"), "r") as sparql_file:
                sparql = sparql_file.read()
                for result in self.__graph.query(sparql):
                    self.__graph.add(result)
        print("Graph after applying rules:")
        self.print_graph()

    def ask(self, triple) -> bool:
        for _ in self.__graph.triples(triple):
            return True
        return False

    def print_graph(self):
        print(self.__graph.serialize(format="ttl").decode("utf-8"))

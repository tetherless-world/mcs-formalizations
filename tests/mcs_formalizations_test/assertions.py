from mcs_formalizations.path import DATA_DIR_PATH
from rdflib import Graph
from pathlib import Path
import bz2

import json
from typing import Optional, Tuple


def assert_valid_rdf_loaded(*, pipeline_id: str, data_dir_path: Path):

    loaded_data_dir_path = data_dir_path / "loaded"
    assert loaded_data_dir_path.is_dir()
    rdf_file_path = loaded_data_dir_path / (pipeline_id + ".ttl")
    assert rdf_file_path.is_file()

    new_graph = Graph()
    with open(rdf_file_path, "rb") as rdf_file:
        new_graph.parse(source=rdf_file, format="ttl")

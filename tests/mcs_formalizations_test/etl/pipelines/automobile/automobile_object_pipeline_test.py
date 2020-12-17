from mcs_formalizations.path import DATA_DIR_PATH
from tests.mcs_formalizations_test.assertions import assert_valid_rdf_loaded
from mcs_formalizations.pipelines.automobile.automobile_object_pipeline import (
    AutomobileObjectPipeline,
)


def test_extract_transform_load():
    AutomobileObjectPipeline(data_dir_path=DATA_DIR_PATH).extract_transform_load()
    assert_valid_rdf_loaded(
        pipeline_id=AutomobileObjectPipeline.ID, data_dir_path=DATA_DIR_PATH
    )

from mcs_formalizations.path import DATA_DIR_PATH
from tests.mcs_formalizations_test.assertions import assert_valid_rdf_loaded
from mcs_formalizations.pipelines.parking_garage.parking_garage_object_pipeline import (
    ParkingGarageObjectPipeline,
)


def test_extract_transform_load():
    ParkingGarageObjectPipeline(data_dir_path=DATA_DIR_PATH).extract_transform_load()
    assert_valid_rdf_loaded(
        pipeline_id=ParkingGarageObjectPipeline.ID, data_dir_path=DATA_DIR_PATH
    )

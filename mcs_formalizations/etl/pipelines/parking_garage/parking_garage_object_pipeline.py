from mcs_formalizations._pipeline import _Pipeline
from mcs_formalizations.path import DATA_DIR_PATH

from pathlib import Path

from mcs_formalizations.nop_extractor import (
    NopExtractor,
)
from mcs_formalizations.pipelines.parking_garage.parking_garage_object_transformer import (
    ParkingGarageObjectTransformer,
)


class ParkingGarageObjectPipeline(_Pipeline):
    ID = "parking_garage"

    def __init__(self, *, data_dir_path: Path = DATA_DIR_PATH, **kwds):
        _Pipeline.__init__(
            self,
            extractor=NopExtractor(pipeline_id=self.ID, **kwds),
            id=self.ID,
            transformer=ParkingGarageObjectTransformer(
                pipeline_id=self.ID, data_dir_path=data_dir_path, **kwds
            ),
            data_dir_path=data_dir_path,
            **kwds,
        )


if __name__ == "__main__":
    ParkingGarageObjectPipeline.main()

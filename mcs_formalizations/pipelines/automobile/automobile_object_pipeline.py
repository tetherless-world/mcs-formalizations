from mcs_formalizations._pipeline import _Pipeline
from mcs_formalizations.path import DATA_DIR_PATH

from pathlib import Path

from mcs_formalizations.nop_extractor import (
    NopExtractor,
)
from mcs_formalizations.pipelines.automobile.automobile_object_transformer import (
    AutomobileObjectTransformer,
)


class AutomobileObjectPipeline(_Pipeline):
    ID = "automobile"

    def __init__(self, *, data_dir_path: Path = DATA_DIR_PATH, **kwds):
        _Pipeline.__init__(
            self,
            extractor=NopExtractor(pipeline_id=self.ID, **kwds),
            id=self.ID,
            transformer=AutomobileObjectTransformer(
                pipeline_id=self.ID, data_dir_path=data_dir_path, **kwds
            ),
            data_dir_path=data_dir_path,
            **kwds,
        )


if __name__ == "__main__":
    AutomobileObjectPipeline.main()

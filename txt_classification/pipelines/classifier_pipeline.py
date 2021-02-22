from mcs_formalizations.etl._pipeline import _Pipeline
from mcs_formalizations.path import DATA_DIR_PATH
from mcs_formalizations.etl._loader import _Loader
from mcs_formalizations.etl.loaders.txt_file_loader import TxtFileLoader
from mcs_formalizations.etl.loaders.csv_file_loader import CsvFileLoader

from pathlib import Path

from txt_classification.classifiers import Classifiers

from txt_classification.extractors.mean_vector_extractor import MeanVectorExtractor
from txt_classification.pipelines.classifier_transformer import ClassifierTransformer


class ClassifierPipeline(_Pipeline):
    ID = "classifier"

    def __init__(
        self, *, annotation_file_path: Path, data_dir_path: Path = DATA_DIR_PATH, **kwds
    ):
        _Pipeline.__init__(
            self,
            extractor=MeanVectorExtractor(
                pipeline_id=self.ID, file_path=annotation_file_path, **kwds
            ),
            id=self.ID,
            transformer=ClassifierTransformer(
                pipeline_id=self.ID, data_dir_path=data_dir_path, **kwds
            ),
            data_dir_path=data_dir_path,
            **kwds,
        )


if __name__ == "__main__":
    ClassifierPipeline.main()

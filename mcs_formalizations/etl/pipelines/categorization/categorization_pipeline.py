from mcs_formalizations.etl._pipeline import _Pipeline
from mcs_formalizations.path import DATA_DIR_PATH

from pathlib import Path

from mcs_formalizations.etl.models.categorization_metadata import CategorizationMetadata

from mcs_formalizations.etl.nop_extractor import (
    NopExtractor,
)
from mcs_formalizations.etl.pipelines.categorization.categorization_transformer import (
    CategorizationTransformer,
)


class CategorizationPipeline(_Pipeline):
    ID = "categorization"

    def __init__(
        self,
        *,
        data_dir_path: Path = DATA_DIR_PATH,
        categorizer_name: str,
        month_num: int,
        day_num: int,
        year_num: int,
        preprocess: bool = True,
        **kwds,
    ):

        categorization_metadata = CategorizationMetadata(
            categorizer_name=categorizer_name,
            month_num=month_num,
            day_num=day_num,
            year_num=year_num,
        )

        formatted_id = (
            f"{self.ID}_{categorizer_name}_{month_num}-{day_num}-{year_num}_preprocessed"
            if preprocess
            else f"{self.ID}_{categorizer_name}_{month_num}-{day_num}-{year_num}_raw"
        )

        _Pipeline.__init__(
            self,
            extractor=NopExtractor(pipeline_id=self.ID, **kwds),
            id=formatted_id,
            transformer=CategorizationTransformer(
                pipeline_id=self.ID,
                data_dir_path=data_dir_path,
                categorization_metadata=categorization_metadata,
                preprocess=preprocess,
                **kwds,
            ),
            data_dir_path=data_dir_path,
            **kwds,
        )


if __name__ == "__main__":
    CategorizationPipeline.main()
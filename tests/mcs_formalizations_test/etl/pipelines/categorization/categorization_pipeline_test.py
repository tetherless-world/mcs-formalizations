from mcs_formalizations.path import DATA_DIR_PATH
from mcs_formalizations.etl.pipelines.categorization.categorization_pipeline import (
    CategorizationPipeline,
)


def test_extract_transform_load():
    CategorizationPipeline(
        data_dir_path=DATA_DIR_PATH,
        categorizer_name="Weighted",
        month_num=12,
        day_num=15,
        year_num=2020,
        preprocess=False,
    ).extract_transform_load()

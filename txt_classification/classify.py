from mcs_formalizations.path import DATA_DIR_PATH
from txt_classification.classifiers import Classifiers
from mcs_formalizations.etl.models.categorization_metadata import CategorizationMetadata
from txt_classification.pipelines.classifier_pipeline import ClassifierPipeline


if __name__ == "__main__":

    categorization_metadata = CategorizationMetadata(
        categorizer_name="Alice",
        month_num=12,
        day_num=15,
        year_num=2020,
        preprocessing="raw",
    )

    # parameters = {"n_estimators": 100}

    # parameters = {"gamma": 2, "C": 1}
    parameters = {}

    ClassifierPipeline(
        classifier_type=Classifiers.QDA,
        parameters=parameters,
        annotation_file_name=f"categorization_{categorization_metadata.categorizer_name}_{categorization_metadata.month_num}-{categorization_metadata.day_num}-{categorization_metadata.year_num}_{categorization_metadata.preprocessing}.csv",
        data_dir_path=DATA_DIR_PATH,
    ).extract_transform_load()

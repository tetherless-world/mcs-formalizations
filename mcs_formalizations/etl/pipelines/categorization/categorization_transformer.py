import csv
from pathlib import Path
from typing import Generator, Dict

from mcs_formalizations.path import DATA_DIR_PATH

from mcs_formalizations.preprocessing import text_process

from mcs_formalizations.etl._model import _Model
from mcs_formalizations.etl._transformer import _Transformer
from mcs_formalizations.helpers import categories
from mcs_formalizations.etl.models.categorization_metadata import CategorizationMetadata
from mcs_formalizations.etl.models.categorization_sample import CategorizationSample


class CategorizationTransformer(_Transformer):
    def __init__(
        self,
        *,
        pipeline_id: str,
        threshold: int,
        data_dir_path: Path = DATA_DIR_PATH,
        categorization_metadata: CategorizationMetadata,
        preprocess: bool,
        **kwds,
    ):
        _Transformer.__init__(
            self, pipeline_id=pipeline_id, data_dir_path=data_dir_path, **kwds
        )
        self.threshold = threshold
        self.categorization_metadata = categorization_metadata
        self.preprocess = preprocess

    def _categorization_csv_file_path(self, *, metadata: CategorizationMetadata):
        """
        returns file path of the type of file indicated by the parameters
        @param dataset_type the type of dataset (i.e. dev, test, train)
        @param content_type the type of information contained in the file (i.e. samples, labels)
        """
        return (
            self._pipeline_data_dir_path
            / f"{metadata.categorizer_name}_Categorization_{metadata.month_num}-{metadata.day_num}-{metadata.year_num}.csv"
        )

    def clean_question(self, *, question: str, preprocess: bool):

        parsed = " ".join(question.split()[3:])

        if preprocess:
            parsed = text_process(parsed)

        return parsed

    def find_categories(self, *, rankings: Dict[str, str]):

        labels = []

        for category, value in rankings.items():
            if value.strip() != "" and int(value) >= self.threshold:
                formatted_category = "-".join(category.split())
                labels.append(formatted_category)

        return labels

    def transform(
        self,
        **kwds,
    ) -> Generator[_Model, None, None]:

        categorization_csv_file_path = self._categorization_csv_file_path(
            metadata=self.categorization_metadata
        )

        with open(categorization_csv_file_path) as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                sample_question = self.clean_question(
                    question=row["question"], preprocess=self.preprocess
                )

                sample_rankings = {key: row[key] for key in categories()}

                sample_labels = self.find_categories(rankings=sample_rankings)

                yield CategorizationSample(
                    sample_question=sample_question,
                    sample_labels=sample_labels,
                )

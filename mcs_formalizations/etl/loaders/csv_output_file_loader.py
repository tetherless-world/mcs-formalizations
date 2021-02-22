from pathlib import Path
from typing import Optional, Generator

from pathvalidate import sanitize_filename
import os
import csv

from tqdm import tqdm

from mcs_formalizations.etl._loader import _Loader
from mcs_formalizations.helpers import categories
from mcs_formalizations.namespace import bind_namespaces
from mcs_formalizations.etl.models.categorization_sample import CategorizationSample


class CsvOutputFileLoader(_Loader):
    def __init__(
        self,
        *,
        compress: bool = True,
        file_path: Optional[Path] = None,
        **kwds,
    ):
        _Loader.__init__(self, **kwds)
        self.__compress = compress
        self.__file_path = file_path

    def load(self, *, models: Generator[CategorizationSample, None, None]):
        file_path = self.__file_path
        if file_path is None:
            file_name_parts = [
                sanitize_filename(self._pipeline_id),
                "csv",
            ]
            file_name = ".".join(file_name_parts)
            file_path = self._loaded_data_dir_path / "csv_outputs" / file_name

        self._logger.info("writing classification results to %s", file_path)

        file_existed = os.path.exists(file_path)

        print(file_existed)

        open_arg = "w"

        if file_existed:
            open_arg = "a"

        print(open_arg)

        header_row = [
            "classifier_type",
            "parameters",
            "file_name",
            "accuracy",
            "balanced_accuracy",
        ]

        with open(file_path, open_arg) as file_:

            writer = csv.writer(file_)

            if file_existed:
                writer.writerow(header_row)

            for results in models:
                results_line = [
                    results.classifier_type,
                    str(results.parameters),
                    results.file_name,
                    results.accuracy,
                    results.balanced_accuracy,
                ]

                writer.writerow(results_line)

        self._logger.info("wrote classification results to %s", file_path)

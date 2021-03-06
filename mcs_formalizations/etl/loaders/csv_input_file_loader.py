from pathlib import Path
from typing import Optional, Generator

from pathvalidate import sanitize_filename
import bz2
import csv

from tqdm import tqdm

from mcs_formalizations.etl._loader import _Loader
from mcs_formalizations.helpers import categories
from mcs_formalizations.namespace import bind_namespaces
from mcs_formalizations.etl.models.categorization_sample import CategorizationSample


class CsvInputFileLoader(_Loader):
    def __init__(
        self,
        *,
        binary: bool = True,
        compress: bool = True,
        file_path: Optional[Path] = None,
        **kwds,
    ):
        _Loader.__init__(self, **kwds)
        self.__binary = binary
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
            file_path = self._loaded_data_dir_path / "csv_inputs" / file_name

        self._logger.info("writing categorizations to %s", file_path)

        header_row = ["sentence"] + categories()

        with open(file_path, "w") as file_:

            writer = csv.writer(file_)
            writer.writerow(header_row)
            for sample in models:
                sample_line = []
                if len(sample.sample_labels) == 0:
                    continue

                sample_line.append('"' + sample.sample_question + '"')
                for category in categories():
                    hyph_category = "-".join(category.split())
                    if hyph_category in sample.sample_labels:
                        if self.__binary:
                            sample_line.append("1")
                        else:
                            sample_line.append("true")
                    else:
                        if self.__binary:
                            sample_line.append("0")
                        else:
                            sample_line.append("false")
                writer.writerow(sample_line)

        self._logger.info("wrote categorizations to %s", file_path)

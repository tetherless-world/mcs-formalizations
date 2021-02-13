from pathlib import Path
from typing import Optional, Generator

from pathvalidate import sanitize_filename
import bz2

from tqdm import tqdm

from mcs_formalizations.etl._loader import _Loader
from mcs_formalizations.namespace import bind_namespaces
from mcs_formalizations.etl.models.categorization_sample import CategorizationSample


class TxtFileLoader(_Loader):
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
                "txt",
            ]
            file_name = ".".join(file_name_parts)
            file_path = self._loaded_data_dir_path / file_name

        self._logger.info("writing categorizations to %s", file_path)
        with open(file_path, "w") as file_:
            for sample in models:
                sample_line = []
                if len(sample.sample_labels) == 0:
                    continue
                for label in sample.sample_labels:
                    sample_line.append(f"__label__{label} ")
                sample_line.append(f"{sample.sample_question}\n")
                sample_text = "".join(sample_line)
                file_.write(sample_text)

        self._logger.info("wrote categorizations to %s", file_path)

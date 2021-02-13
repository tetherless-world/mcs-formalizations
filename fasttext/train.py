import fasttext as ft
from pathlib import path
from mcs_formalizations.path import DATA_DIR_PATH


if __name__ == "__main__":

    #### PARAMETERS #####
    categorizer_name = "Gretchen"
    month_num = 12
    day_num = 18
    year_num = 2020
    preprocessed = True
    #####################

    suffix = "preprocessed.txt" if preprocessed else "raw.txt"

    file_path = (
        DATA_DIR_PATH
        / "loaded"
        / f"categorization_{categorizer_name}_{month_num}-{day_num}-{year_num}_{suffix}"
    )

    model = ft.train_supervised(input=file_path)

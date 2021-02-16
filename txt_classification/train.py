import fasttext as ft
from pathlib import Path
from mcs_formalizations.path import DATA_DIR_PATH


if __name__ == "__main__":

    #### PARAMETERS #####
    categorizer_name = "Gretchen"
    month_num = 12
    day_num = 15
    year_num = 2020
    preprocessed = True
    epochs = 25
    #####################

    suffix = "preprocessed" if preprocessed else "raw"

    ngrams = 1 if preprocessed else 2

    file_path = str(
        DATA_DIR_PATH
        / f"loaded/txt/categorization_{categorizer_name}_{month_num}-{day_num}-{year_num}_{suffix}.txt"
    )

    model = ft.train_supervised(input=file_path, epoch=epochs, wordNgrams=ngrams)

    model.save_model(
        f"./models/model_{categorizer_name}_{month_num}-{day_num}-{year_num}_{suffix}_epochs-{epochs}_ngrams-{ngrams}.bin"
    )

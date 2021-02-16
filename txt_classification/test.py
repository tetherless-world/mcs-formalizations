import fasttext as ft
from pathlib import Path
from csv import writer
from mcs_formalizations.path import DATA_DIR_PATH, ROOT_DIR_PATH
from mcs_formalizations.helpers import categories


def append_list_as_row(file_path, row_list):

    with open(file_path, "a+") as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(row_list)


if __name__ == "__main__":

    #### PARAMETERS #####
    categorizer_name = "Gretchen"
    month_num = 12
    day_num = 15
    year_num = 2020
    preprocessed = True
    epochs = 25
    prompt = "A cat falls out of a tree before it climbs it."
    #####################

    suffix = "preprocessed" if preprocessed else "raw"

    ngrams = 1 if preprocessed else 2

    file_path = str(
        DATA_DIR_PATH
        / f"loaded/categorization_{categorizer_name}_{month_num}-{day_num}-{year_num}_{suffix}.txt"
    )

    model = ft.load_model(
        f"./models/model_{categorizer_name}_{month_num}-{day_num}-{year_num}_{suffix}_epochs-{epochs}_ngrams-{ngrams}.bin"
    )

    labels, probs = model.predict(prompt, k=-1)

    indx = 0

    prob_dict = dict()

    for i in range(len(labels)):
        category = labels[i].split("__")[-1]

        prob_dict[category] = probs[indx]

        indx += 1

    results_list = [
        categorizer_name,
        month_num,
        day_num,
        year_num,
        preprocessed,
        epochs,
        ngrams,
        prompt,
    ]

    for category in categories():
        if category not in prob_dict.keys():
            results_list.append("")
        else:
            results_list.append(prob_dict[category])

    file_path = ROOT_DIR_PATH / f"txt_classification/results/results.csv"

    append_list_as_row(file_path, results_list)

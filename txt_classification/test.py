import fasttext as ft
from pathlib import Path
from csv import writer
from mcs_formalizations.path import DATA_DIR_PATH, ROOT_DIR_PATH
from mcs_formalizations.helpers import categories


def append_list_as_row(file_path, row_list):

    with open(file_path, "a+") as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(row_list)


def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


if __name__ == "__main__":

    #### PARAMETERS #####
    categorizer_name = "Weighted"
    month_num = 12
    day_num = 15
    year_num = 2020
    manipulation = "preprocessed"
    epochs = 25
    prompt = "A cat falls out of a tree before it climbs it."
    #####################

    ngrams = (
        1 if manipulation == "preprocessed" or manipulation == "with_stopwords" else 2
    )

    file_path = str(
        DATA_DIR_PATH
        / f"loaded/txt/testing/categorization_{categorizer_name}_{month_num}-{day_num}-{year_num}_raw.txt"
    )

    model = ft.load_model(
        f"./models/model_{categorizer_name}_{month_num}-{day_num}-{year_num}_raw_epochs-{epochs}_ngrams-2.bin"
    )
    print_results(*model.test(file_path))

    model = ft.load_model(
        f"./models/model_{categorizer_name}_{month_num}-{day_num}-{year_num}_with_stopwords_epochs-{epochs}_ngrams-1.bin"
    )
    print_results(*model.test(file_path))
    model = ft.load_model(
        f"./models/model_{categorizer_name}_{month_num}-{day_num}-{year_num}_preprocessed_epochs-{epochs}_ngrams-1.bin"
    )

    print_results(*model.test(file_path))
    # labels, probs = model.predict(prompt, k=-1)

    # indx = 0

    # prob_dict = dict()

    # for i in range(len(labels)):
    #     category = labels[i].split("__")[-1]

    #     prob_dict[category] = probs[indx]

    #     indx += 1

    # results_list = [
    #     categorizer_name,
    #     month_num,
    #     day_num,
    #     year_num,
    #     manipulation,
    #     epochs,
    #     ngrams,
    #     prompt,
    # ]

    # for category in categories():
    #     if category not in prob_dict.keys():
    #         results_list.append("")
    #     else:
    #         results_list.append(prob_dict[category])

    # file_path = ROOT_DIR_PATH / f"txt_classification/results/results.csv"

    # append_list_as_row(file_path, results_list)

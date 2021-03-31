import csv
from sklearn import metrics
from string import Template
from mcs_formalizations.path import DATA_DIR_PATH


classes_1 = [
    "Time",
    "World states",
    "Events",
    "Space",
    "Physical Entities",
    "Values and quantities",
    "Classes and instances",
    "Sets",
]

classes_2 = [
    "Time",
    "World States",
    "Classes and Instances",
    "Sets",
    "Values and Quantities",
    "Space",
    "Physical entities",
    "Events",
]


annotators = ["Alice", "Gretchen", "Henrique", "Rebecca"]


def print_results(y_true, y_pred):
    results = metrics.precision_recall_fscore_support(y_true, y_pred)
    print("Precision:", results[0])
    print("Recall:", results[1])
    print("f-score:", results[2])
    print(metrics.precision_score(y_true, y_pred, average="weighted"))
    print(metrics.recall_score(y_true, y_pred, average="weighted"))
    print()


def get_scores():

    for name in annotators:

        first_half_old, second_half_old = load_annotator_old(name)

        first_half_new, second_half_new = load_annotator_new(name)

        print(name)

        print_results(first_half_old, first_half_new)
        print_results(second_half_old, second_half_new)


def load_annotator_new(annotator):
    data = []
    path = Template(
        str(DATA_DIR_PATH / "categorization/Alternate-${annotator}-Binary.csv")
    )
    with open(path.substitute(annotator=annotator), "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            labels = []
            for _class in classes_1:
                labels.append(int(row[_class.title()]))
            data.append(labels)

    return data[:100], data[101:]


def load_annotator_old(annotator):
    path = Template(
        str(DATA_DIR_PATH / "categorization/${annotator}_Categorization_12-15-2020.csv")
    )
    data = []
    with open(path.substitute(annotator=annotator), "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        i = 0
        for row in csvreader:
            labels = []
            rank_counts = dict()
            for _class in classes_1:
                if row[_class].strip() == "":
                    continue
                elif int(row[_class]) in rank_counts.keys():
                    rank_counts[int(row[_class])] += 1
                else:
                    rank_counts[int(row[_class])] = 1
            sorted_ranks = sorted(rank_counts.keys(), reverse=True)

            max_labels = []

            if rank_counts[sorted_ranks[0]] == 1 and len(rank_counts) > 1:
                max_labels = [sorted_ranks[0], sorted_ranks[1]]
            else:
                max_labels = [sorted_ranks[0]]

            for _class in classes_1:
                if row[_class].strip() == "" or int(row[_class]) not in max_labels:
                    labels.append(0)
                else:
                    labels.append(1)
            data.append(labels)
            if i == 0:
                print(labels)
            i += 1

    return data[:100], data[101:]


get_scores()

import csv
from sklearn import metrics
from string import Template
from mcs_formalizations.path import DATA_DIR_PATH

truth = []
annotator0 = []
annotator1 = []
annotator2 = []
annotator3 = []
classes = [
    "Time",
    "World states",
    "Events",
    "Space",
    "Physical Entities",
    "Values and quantities",
    "Classes and instances",
    "Sets",
]
annotators = ["Alice", "Gretchen", "Henrique", "Minor", "Rebecca"]


def print_results(y_true, y_pred):
    results = metrics.precision_recall_fscore_support(y_true, y_pred)
    print("Precision:", results[0])
    print("Recall:", results[1])
    print("f-score:", results[2])
    print(metrics.precision_score(y_true, y_pred, average="weighted"))
    print(metrics.recall_score(y_true, y_pred, average="weighted"))
    print()


def get_scores(true_threshold, pred_threshold):

    for name in annotators:

        truth = []

        load_annotator(name, true_threshold, truth)

        others = [i for i in annotators if i != name]

        for other in others:
            annotator = []
            load_annotator(other, pred_threshold, annotator)
            print(name + " vs. " + other)
            print_results(truth, annotator)


def load_annotator(annotator, threshold, data):
    path = Template(
        str(DATA_DIR_PATH / "categorization/${annotator}_Categorization_12-15-2020.csv")
    )
    with open(path.substitute(annotator=annotator), "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            labels = []
            for _class in classes:
                if row[_class].strip() == "" or int(row[_class]) < threshold:
                    labels.append(0)
                else:
                    labels.append(1)
            data.append(labels)


true_threshold = 3
pred_threshold = 1

get_scores(true_threshold, pred_threshold)

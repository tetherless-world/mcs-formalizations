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


def get_scores():

    for name in annotators:

        load_annotator(name, 3, truth)

        others = [i for i in annotators if i != name]

        for other in others:
            load_annotator(other, 1, annotator0)

        print(name + " vs. " + other)
        print(truth)
        results = metrics.precision_recall_fscore_support(truth, annotator0)
        print("Precision:", results[0])
        print("Recall:", results[1])
        print("f-score:", results[2])
        print(metrics.precision_score(truth, annotator0, average="weighted"))
        print(metrics.recall_score(truth, annotator0, average="weighted"))


def load_annotator(annotator, threshold, data):
    path = Template(
        str(
            DATA_DIR_PATH / "/categorization/${annotator}_Categorization_12-15-2020.csv"
        )
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


get_scores()

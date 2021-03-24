import csv
from sklearn import metrics
from string import Template
from mcs_formalizations.path import DATA_DIR_PATH


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

        exercise_one = []
        exercise_two = []

        load_annotator_old(name, exercise_one)

        load_annotator_new(other, exercise_two)
        
        print(name)
        
        print_results(exercise_one, exercise_two)

def load_annotator_new(annotator, data):
    path = Template(
        str(DATA_DIR_PATH / "categorization/Alternate_${annotator}_Binary.csv")
    )
    with open(path.substitute(annotator=annotator), "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            labels = []
            for _class in classes:
                labels.append(int(row[_class]))
            data.append(labels)


def load_annotator_old(annotator, data):
    path = Template(
        str(DATA_DIR_PATH / "categorization/${annotator}_Categorization_12-15-2020.csv")
    )
    with open(path.substitute(annotator=annotator), "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        i = 0
        for row in csvreader:
            labels = []
            rank_counts = dict()
            for _class in classes:
                if int(row[_class]) in rank_counts.keys():
                    rank_counts[int(row[_class])] += 1
                else:
                    rank_counts[int(row[_class])] = 1
            sorted_ranks = sorted(rank_counts.keys(), reverse=True)

            max_labels = []

            if rank_counts[sorted_ranks[0]] =1:
                max_labels = [sorted_ranks[0], sorted_ranks[1]]
            else:
                max_labels = [sorted_ranks[0]]

            for _class in classes:
                if row[_class].strip() == "" or int(row[_class]) not in max_labels:
                    labels.append(0)
                else:
                    labels.append(1)
            data.append(labels)
            if i == 0:
                print(labels)
            i+=1



get_scores()

import pandas as pd
from sklearn import metrics
from mcs_formalizations.path import DATA_DIR_PATH, ROOT_DIR_PATH
import csv
# initials = ["M", "H", "A", "R", "G"]
old_names = ["Minor", "Henrique", "Alice", "Rebecca", "Gretchen"]

annotators = ["Alice", "Gretchen", "Henrique", "Rebecca"]


def get_scores_original(df, file_path):

    for init in old_names:

        y_test = df[init]

        others = [i for i in old_names if i != init]

        accuracy_list = ["Accuracy"]
        balanced_accuracy_list = ["Balanced Accuracy"]
        precision_list = ["Precision"]
        recall_list = ["Recall"]
        f1_list = ["F1 score"]

        for other in others:
            print(init + " vs. " + other)

            y_pred = df[other]

            accuracy_list.append(metrics.accuracy_score(y_test, y_pred))
            balanced_accuracy_list.append(metrics.balanced_accuracy_score(y_test, y_pred))
            precision_list.append(metrics.precision_score(y_test, y_pred))
            recall_list.append(metrics.recall_score(y_test, y_pred))
            f1_list.append(metrics.f1_score(y_test, y_pred))

            # tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()
            # print(tn, fp, fn, tp)
            # print(metrics.classification_report(y_test, y_pred))

        header_row = [init] + others

        with open(file_path, "w") as file_:

            writer = csv.writer(file_)
            writer.writerow(header_row)
            writer.writerow(accuracy_list)
            writer.writerow(balanced_accuracy_list)
            writer.writerow(precision_list)
            writer.writerow(recall_list)
            writer.writerow(f1_list)
            writer.writerow([])




def get_scores_new(df):

    for name in annotators:

        y_test = df[name]

        others = [i for i in annotators if i != name]

        for other in others:
            print(name + " vs. " + other)

            y_pred = df[other]

            print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
            print("Balanced Accuracy:", metrics.balanced_accuracy_score(y_test, y_pred))
            print("Precision:", metrics.precision_score(y_test, y_pred))
            print("Recall:", metrics.recall_score(y_test, y_pred))
            print("F1 score", metrics.f1_score(y_test, y_pred))

            tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()
            print(tn, fp, fn, tp)
            print(metrics.classification_report(y_test, y_pred))



if __name__ == "__main__":

    categories = ['Classes-and-Instances', 'Events', 'Physical-Entities', 'Sets', 'Space', 'Time', 'World-States']
    threshold = 3

    for category in categories:

        with open(DATA_DIR_PATH / f"categorization/{category}_Binary_{threshold}.csv") as csv_file:
            df = pd.read_csv(csv_file)

            # This line is necessary for Alice's summary file.
            # df.drop(df.tail(1).index, inplace=True)

            file_path = ROOT_DIR_PATH / f"txt_classification/results/{category}_{threshold}.csv"

            get_scores_original(df, file_path)

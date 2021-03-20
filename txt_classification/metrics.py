import pandas as pd
from sklearn import metrics
from mcs_formalizations.path import DATA_DIR_PATH

# initials = ["M", "H", "A", "R", "G"]

annotators = ["Alice", "Gretchen", "Henrique", "Rebecca"]


def get_scores_original(df):

    for init in initials:

        y_test = df["Time-" + init]

        others = [i for i in initials if i != init]

        for other in others:
            print(init + " vs. " + other)

            y_pred = df["Time-" + other]

            print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
            print("Balanced Accuracy:", metrics.balanced_accuracy_score(y_test, y_pred))
            print("Precision:", metrics.precision_score(y_test, y_pred))
            print("Recall:", metrics.recall_score(y_test, y_pred))
            print("F1 score", metrics.f1_score(y_test, y_pred))

            tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()
            print(tn, fp, fn, tp)
            print(metrics.classification_report(y_test, y_pred))


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

    with open(
        DATA_DIR_PATH / "categorization/Alternate-Time.csv"
    ) as csv_file:
        df = pd.read_csv(csv_file)

        # This line is necessary for Alice's summary file.
        # df.drop(df.tail(1).index, inplace=True)

        get_scores_new(df)

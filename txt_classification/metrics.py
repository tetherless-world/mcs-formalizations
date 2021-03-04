import pandas as pd
from sklearn import metrics
from mcs_formalizations.path import DATA_DIR_PATH

initials = ["M", "H", "A", "R", "G"]


def get_scores(df):

    for init in initials:

        y_test = df["Physical Entities-" + init]

        others = [i for i in initials if i != init]

        for other in others:

            y_pred = df["Physical Entities-" + other]

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
        DATA_DIR_PATH / "categorization/Binary-PhysicalEntities.csv"
    ) as csv_file:
        df = pd.read_csv(csv_file)

        get_scores(df)

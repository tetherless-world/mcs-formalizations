from enum import Enum


class Classifiers(Enum):
    KNN = "KNeighborsClassifier"
    SVC = "SVC"
    GPC = "GaussianProcessClassifier"
    DTC = "DecisionTreeClassifier"
    RFC = "RandomForestClassifier"
    MLPC = "MLPClassifier"
    ABC = "AdaBoostClassifier"
    GNB = "GaussianNB"
    QDA = "QuadraticDiscriminantAnalysis"

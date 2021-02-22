from enum import Enum

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


class Classifiers(Enum):
    KNN = KNeighborsClassifier
    SVC = SVC
    GPC = GaussianProcessClassifier
    DTC = DecisionTreeClassifier
    RFC = RandomForestClassifier
    MLPC = MLPClassifier
    ABC = AdaBoostClassifier
    GNB = GaussianNB
    QDA = QuadraticDiscriminantAnalysis

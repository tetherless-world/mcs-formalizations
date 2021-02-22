import csv
from pathlib import Path
from typing import Generator, List

from mcs_formalizations.path import DATA_DIR_PATH

from mcs_formalizations.preprocessing import text_process

from mcs_formalizations.etl._model import _Model
from mcs_formalizations.etl._transformer import _Transformer
from mcs_formalizations.etl.models.classification_results import ClassificationResults
from txt_classification.classifiers import Classifiers

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


class ClassifierTransformer(_Transformer):
    def __init__(
        self,
        *,
        pipeline_id: str,
        classifier: Classifiers,
        data_dir_path: Path = DATA_DIR_PATH,
        **kwds,
    ):
        _Transformer.__init__(
            self, pipeline_id=pipeline_id, data_dir_path=data_dir_path, **kwds
        )
        self._classifier = classifier

    def transform(
        self,
        sentence_vecs,
        labels,
        file_name: str,
        **kwds,
    ) -> Generator[_Model, None, None]:

        X_train, X_test, y_train, y_test = train_test_split(
            sentence_vecs, labels, test_size=0.5, random_state=42
        )  # split the data into train and test (features (X) and labels (Y))

        clf = self._classifier(**kwds)  # create a randomforest classifier object

        clf.fit(X_train, y_train)  # train the model with the training data

        y_pred = clf.predict(X_test)  # test the model on the test data

        yield ClassificationResults(
            classifier_type=self._classifier,
            parameters=kwds,
            file_name=file_name,
            accuracy=metrics.accuracy_score(y_test, y_pred),
            balanced_accuracy=metrics.balanced_accuracy_score(y_test, y_pred),
        )

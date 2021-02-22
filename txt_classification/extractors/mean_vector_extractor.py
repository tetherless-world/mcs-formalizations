from pathlib import Path
from typing import Optional
from mcs_formalizations.path import CLASSIFICATION_DIR_PATH

import numpy
import fasttext
import csv

from mcs_formalizations.etl._extractor import _Extractor


class MeanVectorExtractor(_Extractor):
    def __init__(
        self,
        *,
        file_name: Optional[str] = None,
        file_path: Optional[Path] = None,
        **kwds
    ):
        _Extractor.__init__(self, **kwds)
        if file_path is not None:
            self.__file_path = file_path
        elif file_name is not None:
            self.__file_path = self._extracted_data_dir_path / "csv_inputs" / file_name
        else:
            raise ValueError("must specify file_name or file_path")

    def get_mean_vector(self, model, sentence):

        vectors = []

        for word in sentence:  # for each word in a sentence

            vectors.append(
                model.get_word_vector(word)
            )  # get the word vector from the Wikipedia fasttext model

        return numpy.mean(
            vectors, axis=0
        )  # return the mean vector of all words in the sentence

    def append_file_to_data(self, csvfile, model):

        sentence_vectors = []
        labels = []

        spamreader = csv.reader(csvfile)

        for row in spamreader:  # for each line in the csv

            sentence = row[0].split()  # tokenize the sentence in words

            sentence_vectors.append(
                self.get_mean_vector(model, sentence)
            )  # append the sentence vector (mean of all word vectors) to the array of sentence vectors

            labels.append(row[1])  # append the desired label to the array of labels

        return sentence_vectors, labels

    def extract(self, **kwds):
        if not self.__file_path.is_file():
            raise ValueError(str(self.__file_path) + " does not exist")

        model = fasttext.load_model(CLASSIFICATION_DIR_PATH / "models/wiki.en.bin")

        with open(self.__file_path, newline="") as csvfile:

            sentence_vecs, labels = self.append_file_to_data(csvfile, model)

        return {
            "sentence_vecs": sentence_vecs,
            "labels": labels,
            "file_name": self.__file_path.split("//")[-1],
        }

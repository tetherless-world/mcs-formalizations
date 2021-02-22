import csv

import fasttext

import numpy


model = fasttext.load_model(
    "model/wiki.en.bin"
)  # loads the wikipedia model in fasttext
sentence_vectors = []  # initialize the array sentence vectors
labels = []  # initialize the array of labels


def get_mean_vector(model, sentence):
    vectors = []

    for word in sentence:  # for each word in a sentence

        vectors.append(
            model.get_word_vector(word)
        )  # get the word vector from the Wikipedia fasttext model

    return numpy.mean(
        vectors, axis=0
    )  # return the mean vector of all words in the sentence


def append_file_to_data(csvfile):

    spamreader = csv.reader(csvfile)

    for row in spamreader:  # for each line in the csv

        sentence = row[0].split()  # tokenize the sentence in words

        sentence_vectors.append(
            get_mean_vector(model, sentence)
        )  # append the sentence vector (mean of all word vectors) to the array of sentence vectors

        labels.append(row[1])  # append the desired label to the array of labels


with open(
    "data/alice.csv", newline=""
) as csvfile:  # read a CSV file with the annotation

    append_file_to_data(
        csvfile
    )  # append the contents of the file to the sentence vectors and labels


print(len(sentence_vectors))
print(len(labels))

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(
    sentence_vectors, labels, test_size=0.5, random_state=42
)  # split the data into train and test (features (X) and labels (Y))


from sklearn.ensemble import RandomForestClassifier


clf = RandomForestClassifier(
    n_estimators=100
)  # create a randomforest classifier object

clf.fit(X_train, y_train)  # train the model with the training data

y_pred = clf.predict(X_test)  # test the model on the test data


from sklearn import metrics

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))  # calculate accuracy metric

print(
    "Balanced accuracy:", metrics.balanced_accuracy_score(y_test, y_pred)
)  # calculate balanced accuracy metric

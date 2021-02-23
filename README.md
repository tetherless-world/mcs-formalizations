# MCS Formalizations

MCS Formalizations is a set of scripts that can be used to parse the data from categorization exercizes on the CycIC benchmark released on 12/1/2020, transform it into the appropriate format dictated by the fasttext module, and run fastext on the data to produce models that automate the categorization tasks.

For more information on fasttext, including documentation and tutorials, refer to: https://fasttext.cc/.

## One-time Setup

### Create the Python virtual environment

From the current directory:

    python3 -m venv venv

### Activate the virtual environment

On Unix:

    source venv/bin/activate

On Windows:

    venv\Scripts\activate

### Install the dependencies and the project module

    pip install -r requirements.txt
    pip install -e .

### Install the fastText module

    $ git clone https://github.com/facebookresearch/fastText.git
    $ cd fastText
    $ sudo pip install .
    $ # or :
    $ sudo python setup.py install

## Preparing a new categorization file

### 1. Performing the categorization.

Use the following template to perform a categorization: https://docs.google.com/spreadsheets/d/1eqVmxq9ZlOdv0c_vZMwTHfWxaFzqEPevQ2L7vZLA_iQ/edit?usp=sharing

Follow the instructions specified in cell E2 for each of the 7 categories (Time, World States, Events, Space, Physical Entities, Values and Quantities, Classes and instances, and Sets) for each question in column B using the category definitions (https://docs.google.com/document/d/1wZt_L7meLwXwrkB3VrI_xU55Urnrtq_bP2zKnzxT0YI/edit?usp=sharing).

If desired, add a confidence rating, as specified in cell N2. 

### 2. Uploading the categorization.

Once the categorization is complete, download the google sheet as a .csv file and place it in /mcs-formalizations/data/categorizations with a name of the form:

    NAME_Categorization_MM-DD-YYYY.csv

(e.g. Gretchen_Categorization_02-12-2021)


## Producing the fasttext input file

### 1. Adjusting the test file

In a new test file in /tests/mcs_formalizations_test/ets/pipelines/categorization/categorization_pipeline_test.py, adjust the parameters of the function accordingly:

    - loader = "csv" if you are training with Weka, "txt" if you are training with fasttext
    - threshold = the highest ranking that you consider to not be representative of worthy of a label (e.g. a threshold of 3 means that all scores 3 or lower will be disregarded)
    - data_dir_path = DATA_DIR_PATH (likely will not need to change)
    - categorizer_name = NAME
    - month_num = MM
    - day_num = DD
    - year_num = YYYY
    - preprocess = True, if you would like the data to be pre-processed with text parsing tools, False, otherwise

### 2. Producing the file


From the directory, run 

    pytest 

to produce the input files in /data/loaded/FILE_TYPE


## Training the fasttext model

In /txt_classification/train.py, adjust the parameters according to the values set in "1. Adjusting the test file" of the last section.

Consider adjusting the number of epochs that the model is trained through by adjusting the appropriate parameter. See the fastText documentation for more information.

From /txt_classification run

    python train.py

## Testing Classifier Accuracy

In /txt_classification/classify.py, adjust the variables as follows:

    - categorization metadata: select values according to the categorization csv file in /data/loaded/csv_inputs that you want to test with
    - parameters: fill in the parameters for the classifier that you want to classify with (e.g. If you want to use a DecisionTreeClassifier with max_depth of 5, parameters will be {"max_depth":5})
    - ClassifierPipeline.classifier_type: select a classifier based on those defined in /txt_classification/classifiers.py

See https://scikit-learn.org/stable/supervised_learning.html for more information about sklearn classifiers.

From /txt_classification run

    python classify.py

Outputs (accuracy and balanced accuracy) can be found in /data/loaded/csv_outputs/classifier.csv



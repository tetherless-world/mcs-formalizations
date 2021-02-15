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

### Install the dependencies

    pip install -r requirements.txt

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
    categorizer_name = NAME
    month_num = MM
    day_num = DD
    year_num = YYYY
    preprocess = True, if you would like the data to be pre-processed with text parsing tools, False, otherwise

### 2. Producing the file

From the directory, run 

    pytest 

to produce the fasttext input files in /data/loaded


## Training the fasttext model

In /fasttext/train.py, adjust the parameters according to the values set in "1. Adjusting the test file" of the last section.




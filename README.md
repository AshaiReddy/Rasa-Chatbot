# Rasa-Chatbot
A chatbot that takes user queries and returns the best restaurants in the area using Zomato API


# Setup

if you have anaconda installed in your system, please run this command to activate the environment:

```bash 
conda env create -f environment.yml
```

or just refer to requirements.txt for package version information, Python3.7.9 is used.

Mandatory to install these Spacy Models:

``` bash
python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en
```

## Data Files 

data/nlu/nlu.md : contains training examples for the NLU model

data/core/stories.md : contains training stories for the Core model

## Script Files 

zomato : Contains Zomato API integration code

zomato_api.py : Contains functions to consume common Zomato APIs like fetch location details, type of cuisines, search for restaurants, etc
    
actions.py : Contains the following custom actions (insert ZOMATO API key in this script file before starting RASA server)

* search restaurant
* validate location
* validate cuisine
* send email
* restart conversation
* reset slots

nlu_test.py : Contains code to test generated NLU models

rasa_train.py : 

* primary script file to test chatbot from CLI. Contains code to:
* train both NLU and Core model
* persist packaged model in 'models' folder

## Config Files 

config.yml: Contains model configuration and custom policy

domain.yml: Defines chatbot domain like entities, actions, templates, slots

endpoints.yml: Contains the webhook configuration for custom action

smtpconfig.txt: Contains SMTP server configuration information (If using GMAIL, setup account and generate app password) .

## Usage 

### To Invoke Chatbot in Rasa Shell

#### In Terminal 1: 
```bash
rasa run actions
```

#### In Terminal 2: 
```bash
rasa shell
````

### To Invoke Rasa NLU Shell

```bash
rasa shell nlu
```

### To Train the Model: (trains both nlu and core and saves the model in models folder)

```bash 
python3 rasa_train.py
```

MODEL FILE is saved in models folder: (models/restaurant_rasa_model.tar.gz)

NOTE: Both nlu and core model are saved inside one model file, i.e models/restaurant_rasa_model.tar.gz

### To Validate NLU Model Accuracy: (Classification report saved to results/intent_report.json)

    * DEFAULT : separate test set is created
    * VALIDATION : uses cross - validation

```bash python3 nlu_test.py --type DEFAULT```

```bash python3 nlu_test.py --type VALIDATION```


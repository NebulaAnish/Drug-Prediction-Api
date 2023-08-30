# Drug Prediction API

It is a simple api that used Decision Tree Classifier to predict the suitable drug for a patient with given conditions. The features include
- Age
- Sex (0: Female, 1: Male)
- BP Level  (0:HIGH, 1: Low, 2: Normal)
- Cholesterol Level (0:HIGH, 1: Low, 2: Normal)
- Salt Level

The api can be tested by sending post request with these values.

Example request:
Age = 68, Gender = Female, BP= Normal, Cholesterol=Normal and Salt level= 27.10


	POST http://127.0.0.1:8000/?age=68&gender=0&bp=2&cholesterol=2&salt=27.10

## Steps to runserver
- Clone the repository
- Setup the virtual environment:
    `$ conda create --name myenv --file requirements.txt`
- Activate conda environment:
    `$ conda activate myenv`
- Install packages from pip:
    `$ pip install djangorestframework pydotplus`
- Start the server.
    `$python manage.py runserver `

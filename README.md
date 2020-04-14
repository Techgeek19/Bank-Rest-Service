# BANK REST API

## Quick Start Using Pipenv

``` bash
# Activate venv
$ virtualenv env
$ source env/bin/activate

# Install requirements
$ pip3 install -r requirements.txt

# Create DB
'NAME': 'Bank_Details',
'USER': 'postgres',
'PASSWORD': 'rc',
'HOST': 'localhost', 
'PORT': '5432',

$ python manage.py makemigrations
$ python manage,py migrate

# Run Server (http://localhst:8000)
python3 manage.py runserver
```

## Endpoints

* http://localhost:8000/bankapi/<ifsccode>

* http://localhost:8000/bankapi/<bank-name>/<city>

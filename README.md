# 2SmilesBg
(working in progress)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Create a virtual enviroment and activate it using the following code:
```
virtualenv --python=python3 myvenv

source myvenv/bin/activate
```
Install the libraries from the requirements.txt using the following code:

```
pip install -r requirements.txt
```

### Installing

A step by step series of examples that tell you have how I get a development env running

To run locally my app

```
cd SmilesBlog
python manage.py runserver
```

Since the app is being deployed in Heroku, I need to login to heroku using the command prompt and I open the project

```
heroku login
git push heroku master
heroku open
```



## Running the tests

The test part is working in progress..
To run it follow the following instrunctions:

```
cd SmilesBlog
python blog/manage.py test
```

## Authors

* **Manuela Sabatino** - *Initial work* - [ManuCiao](https://github.com/ManuCiao)

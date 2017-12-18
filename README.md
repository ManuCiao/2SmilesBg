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

Install Postgresql-9.6 on your machine (I am using a linux VM - Ubuntu 16.04):
```
sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-9.6
sudo apt-get install postgresql postgresql-contrib
```
To access to the Postgres console I need to type:
```
sudo -u postgres psql
```
To Configure the local database for the Django app I need to create a new database for my app and a new user to whom you will give access to the database:

```
$ sudo -u postgres psql createdb mylocaldb

$ psql
```
Once I am in the database console I create the role and gran the PRIVILEGES:
```
# CREATE ROLE myusername WITH LOGIN PASSWORD ‘mypassword’;

# GRANT ALL PRIVILEGES ON DATABASE mylocaldb TO myusername;
```

To destroy the databasse on your local machine. The simplest way to do this is open a terminal and type:
```
sudo apt-get --purge remove postgresql
```
This will also prompt you to remove that software that depends on Postgres, which in this case it appears you would like to do.
I do not personally run 9.10 or Postgres, so it is possible that Postgres installs itself in several parts. In that case, a simple:
```
dpkg -l | grep postgres
````
Will get you the list of those packages that Postgres installed. Then, just use the same "apt-get --purge remove ...." command but instead of just postgresql, type each package name, separated by spaces, like:

sudo apt-get --purge remove postgresql postgresql-doc postgresql-common (depending on the list of packages installed, of course)


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
heroku git:remote -a mnsabatino-blog #if the app has been already created in Heroku
git push heroku master #deploy coding
heroku open #open the app from the terminal
```

There are some useful commands that can be used to control your Postgres database.

Pull can be used to pull data from your remote Heroku Postgres database to your local machine database.
```
$ heroku pg:pull DATABASE_URL mylocaldb –a myapponheroku
```
It will ask you to create a new database on your local machine.

This command takes the Heroku database of the app myapponheroku and saves its data to a local database in your machine, named mylocaldb.

Push is the inverse of pull, and takes data from your local database and push it to the database in Heroku:
```
$ heroku pg:push mylocaldb DATABASE_URL –a myapponheroku
```
If the remote database is not empty, you will be prompted to reset it with
```
$ heroku pg:reset DATABASE_URL
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

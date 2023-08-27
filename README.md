# Car Rental( CF Challenge) 

This project was bootstrapped with [Django](https://www.djangoproject.com/)

## Pre-requisites

In order to run this project, you must have these dependences installed on your OS:

  * Venv

## Pre-requisites installation
### NOTE: This guide is intended for Linux environments

#### Install Venv

```sh
sudo apt install python3-venv -y
```
#### Create virtual environment

```sh
python -m venv env
```
####  Activate the virtual environment

```sh
source env/bin/activate
```
####  Installs dependencies

```sh
pip install -r requirements.txt
```
### Instructions to start Django server locally:
#

#### Move to src folder

```sh
cd src
```
#### Create the data base

```sh
python manage.py migrate
```
#### Create a super user

```sh
python manage.py createsuperuser
```
#### Start the server

```sh
python manage.py runserver
```
## Learn More

To learn Venv, check out the [Venv documentation](https://docs.python.org/3/library/venv.html).
# ¡Happy coding!

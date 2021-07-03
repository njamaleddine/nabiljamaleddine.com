#!/bin/bash
# Development Setup for nabiljamaleddine
# Assumes the OS is: macOS Sierra
APP_NAME="nabiljamaleddine"

brew install git
brew install python
brew install node

# Create virtual environment
python3 -m venv ~/.virtualenvs/$APP_NAME
source ~/.virtualenvs/${APP_NAME}/bin/activate
pip install --upgrade pip

# create postgresql database
createdb $APP_NAME

# install all python packages
pip install -r requirements-dev.txt

# install node packages
npm install

# run db migrations
python manage.py migrate

# copy over sample env file
cp sample.env .env

# run the application
python manage.py runserver_plus

#!/bin/bash
# Development Setup for nabiljamaleddine
# Assumes the OS is: macOS Sierra
APP_NAME="nabiljamaleddine"

brew install git
brew install python
brew install node

# install global python requirements
sudo pip3 install --upgrade pip
sudo pip3 install virtualenvwrapper

# Create virtual environment
python3 -m venv ~/.virtualenvs/$APP_NAME
source ${APP_NAME}/bin/activate

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

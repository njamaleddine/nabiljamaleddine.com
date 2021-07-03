#!/bin/bash
# Production Setup
APP_NAME="nabiljamaleddine"

# Update and install all packages
./scripts/ubuntu/install_packages.sh

# install global python requirements
sudo pip install --upgrade pip

# Activate Virtual Environment Requirements
python3 -m venv ~/.virtualenvs/$APP_NAME
source ${APP_NAME}/bin/activate
pip install --upgrade pip

# install all production requirements
pip install -r requirements.txt

# install node packages
npm install

# postgres setup (requires manual input)
# export POSTGRES_PASSWORD=$(openssl rand -hex 64)
# sudo -u postgres createuser --interactive
# sudo -u postgres createdb $APP_NAME

# setup .env file
# note, you'll still need to populate some of these variables (see blank ones)
./scripts/setup_env.sh

# run db migrations
python manage.py migrate

# collect static files
./scripts/build_staticfiles.sh

# Setup nginx config
sudo rm /etc/nginx/sites-enabled/default
sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx_default.conf
sudo cp ./nginx.conf /etc/nginx/nginx.conf
sudo nginx -t
sudo touch /srv/${APP_NAME}/access.log
sudo touch /srv/${APP_NAME}/error.log

# copy over and start systemd script
./scripts/update_services.sh

sudo systemctl enable ${APP_NAME}_web

sudo systemctl start ${APP_NAME}_web

#!/bin/bash
# First time setup for .env file
if [ -f ".env" ]; then
    sudo echo "'.env' file already exists, exiting environment variable file setup..."
fi

ENV_FILE=".env"
touch $ENV_FILE
sudo echo 'ALLOWED_HOSTS=""' > ${ENV_FILE}
sudo echo 'DATABASE_URL=""' >> ${ENV_FILE}
sudo echo 'DJANGO_DEBUG=False' >> ${ENV_FILE}
sudo echo 'DJANGO_SECRET_KEY="'$(openssl rand -hex 64)'"' >> ${ENV_FILE}
sudo echo 'SITE_ENVIRONMENT="production"' >> ${ENV_FILE}
sudo echo 'DJANGO_SETTINGS_MODULE="settings.production"' >> ${ENV_FILE}

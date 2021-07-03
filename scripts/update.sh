#!/bin/bash
# Update application
cd /srv/nabiljamaleddine
source ~/.virtualenvs/nabiljamaleddine/bin/activate
git fetch origin
git merge origin/master

npm install

pip install -r requirements.txt
python manage.py migrate

./scripts/build_staticfiles.sh

# copy over and start systemd script
./scripts/update_services.sh

# restart systemd application services
./scripts/restart.sh

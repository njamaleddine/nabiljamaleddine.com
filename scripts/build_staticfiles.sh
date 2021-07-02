#!/bin/bash
sassc app/static/scss/site.scss > app/static/css/site.css
gulp minify
python manage.py collectstatic --no-input
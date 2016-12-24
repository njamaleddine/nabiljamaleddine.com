#!/bin/bash
sassc app/static/scss/site.scss > app/static/css/site.css
gulp minify
yes "yes" | python manage.py collectstatic
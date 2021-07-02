# NabilJamaleddine.com

Version: 1.0.0

NabilJamaleddine.com is a Django Application built with Python 3

## Setup
### Dependencies
* [python](https://www.python.org/)
* [node](https://nodejs.org/en/)

### Project Setup (Assumes macOS)
```
./scripts/dev_setup.sh
```

### Running Application
##### Run with local django server application:
    python manage.py runserver_plus

### Static File Management
1. Compile `scss` into `css`:

        sassc app/static/scss/site.scss > app/static/css/site.css

2. Use gulp to minify the js and css:

        gulp minify

3. Collect static files

        python manage.py collectstatic

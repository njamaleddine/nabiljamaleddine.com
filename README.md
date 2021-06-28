# NabilJamaleddine.com

Version: 1.0.0

NabilJamaleddine.com is a Django Application built using Python 3

## Setup
### Dependencies
1. Install homebrew package manager for macOS. On Linux use the included package manager `apt`, etc.

2. Install [git](https://git-scm.com/)

        brew install git

3. Install [python](https://www.python.org/)

        brew install python

4. Install [node](https://nodejs.org/en/)
        brew install node


### Project Setup
1. Create a virtualenv:

        python3 -m venv ~/.virtualenvs/nabiljamaleddine

2. Activate virtualenv:

        source ~/.virtualenvs/nabiljamaleddine/bin/activate

3. Install requirements:

        pip install -r requirements-dev.txt

4. Copy `sample.env` to `.env`


### Running Application
##### Run with local django server application:
    python manage.py runserver_plus

##### Run as production application using `gunicorn`:
    honcho start


### Static File Management
1. Compile `scss` into `css`:

        sassc app/static/scss/site.scss > app/static/css/site.css

2. Use gulp to minify the js and css:

        gulp minify

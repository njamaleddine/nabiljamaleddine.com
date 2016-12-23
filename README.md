# NabilJamaleddine.com

Version: 1.0.0

NabilJamaleddine.com is a Django 1.10.4 Application built using Python 3.5.2

## Setup

Project Setup is only supported on OS X

### Project Dependencies
1. Install homebrew package manager. On Linux use the included package manager `apt`, etc.
On OS X, Homebrew makes it very simple for us to install many of the project dependencies.

2. Install [git](https://git-scm.com/)

        brew install git

3. Install [python](https://www.python.org/)

        brew install python

4. Install [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/index.html)

        sudo pip install virtualenvwrapper

    * Note: **Don't install any other dependencies using `sudo` after this. [Read more about virtual environments here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)**

6. Install [node](https://nodejs.org/en/)
        brew install node


### Project Setup
1. Clone repository:

        git clone git@bitbucket.org:njamaleddine/nabiljamaleddine.git

2. Create a virtualenv:

        mkvirtualenv nabiljamaleddine

3. Activate virtualenv:

        workon nabiljamaleddine

4. Install requirements:

        pip install -r requirements.txt

5. Copy `sample.env` to `.env`


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

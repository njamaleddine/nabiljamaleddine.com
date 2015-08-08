# Nabil Jamaleddine Website

#### NabilJamaleddine.com is a Flask 0.10.0 Application built using Python 2

##### Project Setup is only supported on Linux/OS X


### Project Dependencies
1. Install homebrew package manager. On Linux use the included package manager `apt`, etc. Homebrew should make it very simple for us to install most of the project dependencies.

2. Install [git](https://git-scm.com/)

        `brew install git`

3. Install [python](https://www.python.org/)

        `brew install python`


4. Install [heroku toolbelt](https://toolbelt.heroku.com/)

        `brew install heroku-toolbelt`

5. Install [Foreman](http://ddollar.github.io/foreman/) (**Must have [Ruby](https://www.ruby-lang.org/en/) installed on machine**)

        `gem install foreman`

6. Install [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/index.html)

        `sudo pip install virtualenvwrapper`

    * Note: **Don't install any other dependencies using `sudo` after this. [Read more about virtual environments here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)**

### Project Setup
1. Clone repository:

        `git clone git@bitbucket.org:njamaleddine/nabiljamaleddine.git`

2. Create a virtualenv:

        `mkvirtualenv nabiljamaleddine`

3. Activate virtualenv:

        `workon nabiljamaleddine`

4. Install requirements:

        `pip install -r requirements.txt`

5. Copy `sample.env` to `.env`


### Running Application
##### Run as local application:
    `foreman start -f Procfile.dev`

##### Run as production application:
    `foreman start`

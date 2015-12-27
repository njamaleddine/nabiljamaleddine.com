# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

import os

from flask import Flask
from flask_mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

from .utils import get_env, load_env_file


# Load environment variables
load_env_file('.env')

APP_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.abspath(os.path.dirname('app'))
AUTHOR = 'Nabil Jamaleddine'

app = Flask(__name__)
app.config.update(
    DEBUG=get_env('DEBUG', False),
    SECRET_KEY=get_env('SECRET_KEY', 'REPLACE_THIS'),
    MAIL_DEFAULT_SENDER="noreply@nabiljamaleddine.com",
    MAIL_SUPPRESS_SEND=False,
    ADMIN_EMAIL=get_env('ADMIN_EMAIL', None),
    MAIL_SERVER=get_env('MAIL_SERVER', 'localhost'),
    MAIL_DEBUG=get_env('MAIL_DEBUG', False),
    MAIL_PORT=get_env('MAIL_PORT', 25),
    MAIL_USE_TLS=get_env('MAIL_USE_TLS', False),
    MAIL_USE_SSL=get_env('MAIL_USE_SSL', False),
    MAIL_USERNAME=get_env('MAIL_USERNAME', None),
    MAIL_PASSWORD=get_env('MAIL_PASSWORD', None),
    MAIL_MAX_EMAILS=get_env('MAIL_MAX_EMAILS', None),
    MAIL_ASCII_ATTACHMENTS=get_env('MAIL_ASCII_ATTACHMENTS', None),
    MAIL_FAIL_SILENTLY=get_env('MAIL_FAIL_SILENTLY', False),
    SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(
        os.path.join(BASE_DIR, 'app.db')
    ),
    SQLALCHEMY_TRACK_MODIFICATIONS=get_env('DEBUG', False)
)
mail = Mail(app)
CsrfProtect(app)
db = SQLAlchemy(app)

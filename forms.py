from __future__ import print_function, unicode_literals

from flask_wtf import Form
from flask.ext.wtf.html5 import EmailField
from wtforms import StringField, widgets
from wtforms import validators as wtfvalidators


class ContactForm(Form):
    name = StringField(
        'name',
        validators=[wtfvalidators.Required()],
    )
    email = EmailField(
        'email',
        validators=[
            wtfvalidators.Required(),
            wtfvalidators.Email(message="Please enter a valid email address")
        ]
    )
    subject = StringField(
        'subject',
        validators=[wtfvalidators.Required()],
    )
    message = StringField(
        'message',
        validators=[wtfvalidators.Required()],
        widget=widgets.TextArea()
    )

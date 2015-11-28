from flask_wtf import Form
from flask.ext.wtf.html5 import EmailField
from wtforms import StringField, widgets
from wtforms import validators as wtfvalidators


class ContactForm(Form):
    name = StringField(
        'name',
        validators=[wtfvalidators.DataRequired()],
    )
    email = EmailField(
        'email', validators=[
            wtfvalidators.DataRequired(),
            wtfvalidators.Email(message="Please enter a valid email address")
        ]
    )
    subject = StringField(
        'subject', validators=[wtfvalidators.DataRequired()],
    )
    message = StringField(
        'message',
        validators=[wtfvalidators.DataRequired()],
        widget=widgets.TextArea()
    )

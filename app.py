# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from flask import Flask, render_template, url_for, redirect, request
from flask_mail import Mail, Message
from flask_wtf.csrf import CsrfProtect

from utils.toolbelt import get_env, load_env_file, strip_html

from forms import ContactForm


# Load environment variables
load_env_file('.env')

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
    MAIL_FAIL_SILENTLY=get_env('MAIL_FAIL_SILENTLY', False)
)
mail = Mail(app)
CsrfProtect(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """ Homepage """
    form = ContactForm(request.form)

    if request.method == 'POST' and form.validate():
        # data sanitization
        name = strip_html(form.name.data)
        email = strip_html(form.email.data)
        subject = strip_html(form.subject.data)
        message = strip_html(form.message.data)

        msg = Message(
            subject,
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=[app.config['ADMIN_EMAIL']]
        )

        msg.body = 'New message from {}\nEmail: {}\n\nMessage:\n{}'.format(
            name, email, message
        )
        msg.html = (
            '<p style="font-weight: bold">New message from {}</p>'
            '<p>Email: {}</p><br/><p>Message:</p><p>{}</p>'
        ).format(name, email, message)

        mail.send(msg)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()

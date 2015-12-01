from __future__ import print_function, unicode_literals

import os

from flask import Flask, render_template, url_for, redirect, request
from flask_mail import Mail, Message
from flask_wtf.csrf import CsrfProtect

from utils.toolbelt import coerce_bool, coerce_int, load_env_file, strip_html

from forms import ContactForm


app = Flask(__name__)

CsrfProtect(app)

app.config.update(
    DEBUG=coerce_bool(os.environ.get('DEBUG', False)),
    SECRET_KEY=os.environ.get('SECRET_KEY', 'REPLACE_THIS'),
    MAIL_DEFAULT_SENDER="noreply@nabiljamaleddine.com",
    MAIL_SUPPRESS_SEND=False,
    ADMIN_EMAIL=os.environ.get('ADMIN_EMAIL', None),
    MAIL_SERVER=os.environ.get('MAIL_SERVER', 'localhost'),
    MAIL_DEBUG=coerce_bool(os.environ.get('MAIL_DEBUG', False)),
    MAIL_PORT=coerce_int(os.environ.get('MAIL_PORT', 25)),
    MAIL_USE_TLS=coerce_bool(os.environ.get('MAIL_USE_TLS', False)),
    MAIL_USE_SSL=coerce_bool(os.environ.get('MAIL_USE_SSL', False)),
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME', None),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD', None),
    MAIL_MAX_EMAILS=os.environ.get('MAIL_MAX_EMAILS', None),
    MAIL_ASCII_ATTACHMENTS=os.environ.get('MAIL_ASCII_ATTACHMENTS', None),
    MAIL_FAIL_SILENTLY=coerce_bool(os.environ.get('MAIL_FAIL_SILENTLY', False))
)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """ Homepage """
    form = ContactForm(request.form)

    if request.method == 'POST' and form.validate():
        # data sanitization
        name = strip_html(form.name.data)
        email = strip_html(form.email.data)
        message = strip_html(form.message.data)

        msg = Message(
            form.subject.data,
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=[app.config['ADMIN_EMAIL']]
        )

        msg.body = 'New message from {}\nEmail: {}\n\nMessage:\n{}'.format(
            name, email, message
        )
        msg.html = (
            '<p><b>New message from {}</b></p>'
            '<p>Email: {}</p><br/><p>Message:</p><p>{}</p>'
        ).format(name, email, message)

        mail.send(msg)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    load_env_file('.env')
    app.run()

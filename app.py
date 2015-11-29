from __future__ import print_function, unicode_literals

import os

from flask import Flask, render_template, url_for, redirect, request
from flask_mail import Mail, Message
from flask_wtf.csrf import CsrfProtect

from utils.toolbelt import coerce_bool, load_env_file

from forms import ContactForm


app = Flask(__name__)

CsrfProtect(app)

app.config.update(
    DEBUG=coerce_bool(os.environ.get('DEBUG', False)),
    SECRET_KEY=os.environ.get('SECRET_KEY', 'REPLACE_THIS'),
    MAIL_DEFAULT_SENDER="noreply@nabiljamaleddine.com",
    MAIL_SUPPRESS_SEND=False,
    ADMIN_EMAIL=os.environ.get('ADMIN_EMAIL', None),
    MAIL_SERVER='localhost',
    MAIL_DEBUG=app.debug,
    MAIL_PORT=25,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=None,
    MAIL_PASSWORD=None,
    MAIL_MAX_EMAILS=None,
    MAIL_ASCII_ATTACHMENTS=False,
)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """ Homepage """
    form = ContactForm(request.form)

    if request.method == 'POST' and form.validate():
        msg = Message(
            form.subject.data,
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=[app.config['ADMIN_EMAIL']]
        )

        msg.body = 'New message from {}\nEmail: {}\n\nMessage:\n{}'.format(
            form.name.data, form.email.data, form.message.data
        )
        msg.html = (
            '<p><b>New message from {}</b></p>'
            '<p>Email: {}</p><br/><p>Message:</p><p>{}</p>'
        ).format(form.name.data, form.email.data, form.message.data)

        mail.send(msg)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    load_env_file('.env')
    app.run()

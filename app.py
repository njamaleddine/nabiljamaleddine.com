import os

from flask import Flask, render_template, url_for, redirect, request
from flask_mail import Mail, Message

from utils.toolbelt import coerce_bool

from forms import ContactForm


app = Flask(__name__)

app.config.update(
    DEBUG=coerce_bool(os.environ.get('DEBUG', False)),
    SECRET_KEY=os.environ.get('SECRET_KEY', 'REPLACE_THIS'),
    DEFAULT_MAIL_SENDER="noreply@nabiljamaleddine.com",
    MAIL_SUPPRESS_SEND=False,
    MAIL_DEBUG=False,
    ADMIN_EMAIL="nabiljamaleddine@gmail.com",
)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """ Homepage """
    form = ContactForm(request.form)
    app.logger.info(form)
    if request.method == 'POST' and form.validate():
        msg = Message(
            form.subject.data,
            sender=app.config['DEFAULT_MAIL_SENDER'],
            recipients=[app.config['ADMIN_EMAIL']]
        )

        app.logger.info(form.name.data)
        app.logger.info(form.email.data)
        app.logger.info(form.message.data)

        msg.body = u"New message from {}\nEmail: {}\n\nMessage:\n{}".format(
            form.name.data, form.email.data, form.message.data
        )
        msg.html = (
            "<p><b>New message from {}</b></p>"
            "<p>Email: {}</p><br/><p>Message:</p><p>{}</p>"
        ).format(form.name.data, form.email.data, form.message.data)

        mail.send(msg)
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()

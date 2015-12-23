# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import json

from flask import Flask, render_template, url_for, redirect, request, abort
from flask_mail import Mail, Message
from flask_wtf.csrf import CsrfProtect

from markdown import Markdown

from forms import ContactForm
from utils.toolbelt import get_env, load_env_file, strip_html


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
    context = {
        'page': 'index'
    }
    context['form'] = form = ContactForm(request.form)

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


@app.route('/blog', methods=['GET'])
def blog():
    """ Display all blog posts from a static json file """
    context = {
        'page': 'blog'
    }
    context['posts'] = []
    with open('static/blog/_posts.json') as json_file:
        context['posts'] = json.load(json_file)
    return render_template('blog.html', **context)


@app.route('/blog/<slug>', methods=['GET'])
def blog_post(slug):
    """
    Return a single blog post and read the content from a markdown file

    Blog post slugs are unique
    """
    context = {
        'page': 'blog_post'
    }
    with open('static/blog/_posts.json') as json_file:
        posts = json.load(json_file)
        for post in posts:
            if post.get('slug') == slug:
                context['post'] = post
                post_markdown_file_path = 'static/blog/{}.md'.format(slug)
                with open(post_markdown_file_path) as post_content:
                    # convert blog post markdown into html
                    post['content'] = Markdown(
                        extensions=[
                            'markdown.extensions.fenced_code',
                            'markdown.extensions.codehilite'
                        ]
                    ).convert(post_content.read())
                return render_template('blog_post.html', **context)
        abort(404)

if __name__ == '__main__':
    app.run()

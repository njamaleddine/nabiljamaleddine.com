# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

import os

from flask import render_template, url_for, redirect, request, abort
from flask_mail import Message

from markdown import Markdown

from .config import app, mail, APP_DIR
from .forms import ContactForm
from .utils import strip_html
from .models import Post, Tag


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
    tag_params = request.args.get('tags')
    if tag_params:
        tags = tag_params.split(',')
        for tag in tags:
            posts = Post.query.order_by(Post.created.desc()).filter(
                Post.tags.any(Tag.name.contains(tag))
            )
    else:
        posts = Post.query.order_by(Post.created.desc()).all()
    context['posts'] = posts
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
    post = Post.query.filter_by(slug=slug).first()
    if post:
        context['post'] = post
        with open(os.path.join(APP_DIR, post.file_upload)) as post_content:
            # convert blog post markdown into html
            context['content'] = Markdown(
                extensions=[
                    'markdown.extensions.fenced_code',
                    'markdown.extensions.codehilite'
                ]
            ).convert(post_content.read())
        return render_template('blog_post.html', **context)
    abort(404)

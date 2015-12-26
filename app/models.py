# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from datetime import datetime

import pytz

from .config import db, AUTHOR
from .utils import strip_non_alphanumeric


tags = db.Table(
    'tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)


class Post(db.Model):
    """ A Blog post """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    slug = db.Column(db.String(100), unique=True)
    summary = db.Column(db.String(255))
    file_upload = db.Column(db.String(255))
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime, onupdate=datetime.utcnow)
    tags = db.relationship(
        'Tag', secondary=tags, backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title, author, summary, file_upload, created=None):
        self.title = title
        self.author = author
        self.slug = self.create_slug(title)
        self.summary = summary
        self.file_upload = file_upload
        self.created = created or datetime.utcnow(tzinfo=pytz.utc)

    def __repr__(self):
        return '<Post %r>' % self.title

    def create_slug(self, slug):
        """ Creates a unique slug for the post """
        return strip_non_alphanumeric(self.title, replace='-', lowercase=True)

    @staticmethod
    def create_post(title, summary, file_upload, author=AUTHOR, tags=[], created=None):
        """ Convenience method to create a blog post with tags """
        post = Post(
            title=title,
            author=author,
            summary=summary,
            file_upload=file_upload,
            created=created
        )

        for tag in tags:
            tag_object = Tag.query.filter_by(name=tag).first()
            if not tag_object:
                # Create the tag if it doesn't exist in the database
                tag_object = Tag(name=tag)
            post.tags.append(tag_object)

        db.session.add(post)
        db.session.commit()
        print(post)


class Tag(db.Model):
    """ A Tag associated with a Post """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name

# -*- coding: utf-8 -*-
from django.test import TestCase

from app.users.models import User
from .factories import UserFactory


class UserTestCase(TestCase):

    def test__str__(self):
        user = UserFactory()
        assert str(user) == user.username

    def test_create_user(self):
        user = User.objects.create_user(
            username='johndoe', email='john@cnn.com', password='a',
            first_name="John", last_name='Doe'
        )
        assert user.is_active is True
        assert user.is_staff is False
        assert user.is_superuser is False
        assert user.email == 'john@cnn.com'
        assert user.get_full_name() == 'John Doe'
        assert user.get_short_name() == 'John'
        assert user.username == 'johndoe'

    def test_create_super_user(self):
        user = User.objects.create_superuser(
            username='admin', email='john@cnn.com', password='abc'
        )
        assert user.is_active is True
        assert user.is_staff is True
        assert user.is_superuser is True

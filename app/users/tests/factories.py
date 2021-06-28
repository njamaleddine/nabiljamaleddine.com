# -*- coding: utf-8 -*-
import factory
from faker import Faker

from app.users.models import User


fake = Faker()
TEST_PASSWORD = fake.password(
    length=10, special_chars=True, digits=True, upper_case=True,
    lower_case=True
)


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f'user-{n}')
    email = factory.Sequence(lambda n: f'user-{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', TEST_PASSWORD)
    first_name = factory.lazy_attribute(lambda x: fake.first_name())
    last_name = factory.lazy_attribute(lambda x: fake.last_name())

    class Meta:
        model = User
        django_get_or_create = ('username', )

import pytest
from django.contrib.auth.models import User
from faker import Faker

faker = Faker()


@pytest.mark.django_db
@pytest.fixture
def base_user():
    user = User.objects.create_user(
        email=faker.email(), password=faker.password(), username=faker.name()
    )
    return user


@pytest.mark.django_db
@pytest.fixture
def admin_user():
    user = User.objects.create_superuser(
        email=faker.email(), password=faker.password(), username=faker.name()
    )
    return user

import pytest
from django_dynamic_fixture import G
from faker import Faker
from rest_framework.exceptions import ValidationError

from libraries.models import Libraries, Bookshelves
from libraries.serializers import (
    LibrariesSerializer,
    BookshelvesCreateSerializer,
    LibrariesBaseSerializer,
    BookshelvesBaseSerializer,
    BooksCreateSerializer,
)

faker = Faker()


@pytest.mark.django_db
def test_libraries_serializer():
    data = {"name": faker.company(), "address": faker.address()}
    serializer = LibrariesSerializer(data=data)
    serializer.is_valid()
    serializer.save()
    assert Libraries.objects.count() == 1


@pytest.mark.django_db
def test_libraries_base_serializer():
    librariy_db = G(Libraries)
    serializer = LibrariesBaseSerializer(librariy_db)
    assert serializer.data == {"id": librariy_db.id, "name": librariy_db.name}


@pytest.mark.django_db
def test_bookshelves_create_serializer():
    librariy_db = G(Libraries)
    data = {"number": faker.random_int(min=1), "library_id": librariy_db.id}
    serializer = BookshelvesCreateSerializer(data=data)
    serializer.is_valid()
    serializer.save()
    assert Bookshelves.objects.count() == 1


@pytest.mark.django_db
def test_bookshelves_create_serializer_wrong_number():
    librariy_db = G(Libraries)
    data = {"number": 0, "library_id": librariy_db.id}
    serializer = BookshelvesCreateSerializer(data=data)

    with pytest.raises(ValidationError) as excinfo:
        serializer.is_valid(raise_exception=True)

    assert "Ensure this value is greater than or equal to 1" in str(excinfo.value)


@pytest.mark.django_db
def test_bookshelves_create_serializer_wrong_library_id():
    data = {"number": faker.random_int(min=1), "library_id": faker.random_int(min=100)}
    serializer = BookshelvesCreateSerializer(data=data)

    with pytest.raises(ValidationError) as excinfo:
        serializer.is_valid(raise_exception=True)

    assert "Invalid library_id" in str(excinfo.value)


@pytest.mark.django_db
def test_bookshelves_base_serializer():
    bookshelves_db = G(Bookshelves)
    serializer = BookshelvesBaseSerializer(bookshelves_db)
    assert serializer.data == {"id": bookshelves_db.id, "number": bookshelves_db.number}


@pytest.mark.django_db
def test_books_create_serializer():
    bookshelves_db = G(Bookshelves)
    data = {
        "name": faker.name(),
        "author": faker.name(),
        "year": faker.random_int(min=1900, max=2100),
        "bookshelf_id": bookshelves_db.id,
    }
    serializer = BooksCreateSerializer(data=data)
    serializer.is_valid()
    serializer.save()
    assert Bookshelves.objects.count() == 1


@pytest.mark.django_db
def test_books_create_serializer_wrong_year():
    bookshelves_db = G(Bookshelves)

    # Too small value

    data = {
        "name": faker.name(),
        "author": faker.name(),
        "year": 1899,
        "bookshelf_id": bookshelves_db.id,
    }
    serializer = BooksCreateSerializer(data=data)
    with pytest.raises(ValidationError) as excinfo:
        serializer.is_valid(raise_exception=True)

    assert "Ensure this value is greater than or equal to 1900" in str(excinfo.value)

    # Too big value

    data["year"] = 2101

    serializer = BooksCreateSerializer(data=data)
    with pytest.raises(ValidationError) as excinfo:
        serializer.is_valid(raise_exception=True)

    assert "Ensure this value is less than or equal to 2100" in str(excinfo.value)


@pytest.mark.django_db
def test_books_create_serializer_wrong_bookshelf_id():

    data = {
        "name": faker.name(),
        "author": faker.name(),
        "year": faker.random_int(min=1900, max=2100),
        "bookshelf_id": faker.random_int(min=100),
    }
    serializer = BooksCreateSerializer(data=data)

    with pytest.raises(ValidationError) as excinfo:
        serializer.is_valid(raise_exception=True)

    assert "Invalid bookshelf_id" in str(excinfo.value)

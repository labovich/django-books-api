import json

import pytest
from django.urls import reverse
from django_dynamic_fixture import G
from faker import Faker
from rest_framework import status
from rest_framework.test import APIRequestFactory

from libraries.models import Libraries, Bookshelves, Books
from libraries.views import LibrariesViewSet, BookshelvesViewSet, BooksViewSet

faker = Faker()


@pytest.mark.django_db
def test_create_libraries():
    request_data = {"name": faker.company(), "address": faker.address()}
    request = APIRequestFactory().post(
        reverse("libraries-list"),
        json.dumps(request_data),
        content_type="application/json",
    )
    response = LibrariesViewSet.as_view({"post": "create"})(request)
    assert response.status_code == status.HTTP_201_CREATED
    assert Libraries.objects.count() == 1


@pytest.mark.django_db
def test_get_libraries():
    libraries_list = []

    for _ in range(faker.random_int(min=2, max=5)):
        libraries_list.append(G(Libraries))

    request = APIRequestFactory().get(
        reverse("libraries-list"),
        content_type="application/json",
    )
    response = LibrariesViewSet.as_view({"get": "list"})(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == len(libraries_list)


@pytest.mark.django_db
def test_get_library_detail():
    librariy_db = G(Libraries)

    request = APIRequestFactory().get(
        reverse("libraries-detail", kwargs={"pk": librariy_db.pk}),
        format="json",
    )
    response = LibrariesViewSet.as_view({"get": "retrieve"})(request, pk=librariy_db.pk)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_library():
    librariy_db = G(Libraries)

    request_data = {"name": faker.company(), "address": faker.address()}

    request = APIRequestFactory().patch(
        reverse("libraries-detail", kwargs={"pk": librariy_db.pk}),
        json.dumps(request_data),
        content_type="application/json",
    )
    response = LibrariesViewSet.as_view({"patch": "update"})(request, pk=librariy_db.pk)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == request_data["name"]


@pytest.mark.django_db
def test_delete_library():
    librariy_db = G(Libraries)

    request = APIRequestFactory().delete(
        reverse("libraries-detail", kwargs={"pk": librariy_db.pk})
    )
    assumption_view = LibrariesViewSet.as_view({"delete": "destroy"})(
        request, pk=librariy_db.pk
    )
    assert assumption_view.status_code == 204
    assert not Libraries.objects.count()


@pytest.mark.django_db
def test_create_bookshelves():
    librariy_db = G(Libraries)
    request_data = {"number": faker.random_int(min=1), "library_id": librariy_db.id}

    request = APIRequestFactory().post(
        reverse("bookshelves-list"),
        json.dumps(request_data),
        content_type="application/json",
    )
    response = BookshelvesViewSet.as_view({"post": "create"})(request)
    assert response.status_code == status.HTTP_201_CREATED
    assert Bookshelves.objects.count() == 1


@pytest.mark.django_db
def test_get_bookshelves():
    bookshelves_list = []

    for _ in range(faker.random_int(min=2, max=5)):
        bookshelves_list.append(G(Bookshelves))

    request = APIRequestFactory().get(
        reverse("bookshelves-list"),
        content_type="application/json",
    )
    response = BookshelvesViewSet.as_view({"get": "list"})(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == len(bookshelves_list)


@pytest.mark.django_db
def test_get_bookshelves_detail():
    bookshelf_db = G(Bookshelves)

    request = APIRequestFactory().get(
        reverse("bookshelves-detail", kwargs={"pk": bookshelf_db.pk}),
        format="json",
    )
    response = BookshelvesViewSet.as_view({"get": "retrieve"})(
        request, pk=bookshelf_db.pk
    )
    print(response.data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_bookshelf():
    bookshelf_db = G(Bookshelves)
    librariy_db = G(Libraries)
    request_data = {"number": faker.random_int(min=1), "library_id": librariy_db.id}

    request = APIRequestFactory().patch(
        reverse("bookshelves-detail", kwargs={"pk": bookshelf_db.pk}),
        json.dumps(request_data),
        content_type="application/json",
    )
    response = BookshelvesViewSet.as_view({"patch": "update"})(
        request, pk=bookshelf_db.pk
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["number"] == request_data["number"]


@pytest.mark.django_db
def test_delete_bookshelf():
    bookshelf_db = G(Bookshelves)

    request = APIRequestFactory().delete(
        reverse("bookshelves-detail", kwargs={"pk": bookshelf_db.pk})
    )
    assumption_view = BookshelvesViewSet.as_view({"delete": "destroy"})(
        request, pk=bookshelf_db.pk
    )
    assert assumption_view.status_code == 204
    assert not Bookshelves.objects.count()


@pytest.mark.django_db
def test_create_book():
    bookshelves_db = G(Bookshelves)
    request_data = {
        "name": faker.name(),
        "author": faker.name(),
        "year": faker.random_int(min=1900, max=2100),
        "bookshelf_id": bookshelves_db.id,
    }

    request = APIRequestFactory().post(
        reverse("books-list"),
        json.dumps(request_data),
        content_type="application/json",
    )
    response = BooksViewSet.as_view({"post": "create"})(request)
    assert response.status_code == status.HTTP_201_CREATED
    assert Books.objects.count() == 1


@pytest.mark.django_db
def test_get_bookshelves():
    books_list = []

    for _ in range(faker.random_int(min=2, max=5)):
        books_list.append(G(Books))

    request = APIRequestFactory().get(
        reverse("books-list"),
        content_type="application/json",
    )
    response = BooksViewSet.as_view({"get": "list"})(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == len(books_list)


@pytest.mark.django_db
def test_get_bookshelves_detail():
    books_db = G(Books)

    request = APIRequestFactory().get(
        reverse("books-detail", kwargs={"pk": books_db.pk}),
        format="json",
    )
    response = BooksViewSet.as_view({"get": "retrieve"})(request, pk=books_db.pk)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_bookshelf():
    books_db = G(Books)
    bookshelf_db = G(Bookshelves)
    request_data = {
        "name": faker.name(),
        "author": faker.name(),
        "year": faker.random_int(min=1900, max=2100),
        "bookshelf_id": bookshelf_db.id,
    }

    request = APIRequestFactory().patch(
        reverse("books-detail", kwargs={"pk": books_db.pk}),
        json.dumps(request_data),
        content_type="application/json",
    )
    response = BooksViewSet.as_view({"patch": "update"})(request, pk=books_db.pk)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == request_data["name"]


@pytest.mark.django_db
def test_delete_books():
    books_db = G(Books)

    request = APIRequestFactory().delete(
        reverse("books-detail", kwargs={"pk": books_db.pk})
    )
    assumption_view = BooksViewSet.as_view({"delete": "destroy"})(
        request, pk=books_db.pk
    )
    assert assumption_view.status_code == 204
    assert not Books.objects.count()

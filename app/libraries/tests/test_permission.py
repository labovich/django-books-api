from unittest.mock import patch

import pytest


from libraries.permissions import IsAdminCreateIsAuthenticatedRead
from libraries.tests.fixtures import admin_user, base_user


@pytest.mark.django_db
@patch("django.http.request.HttpRequest")
def test_permission_for_admin(mocked_request, admin_user):
    mocked_request.method = "POST"
    mocked_request.user = admin_user
    assert IsAdminCreateIsAuthenticatedRead().has_permission(mocked_request, None)

    mocked_request.method = "PUT"
    assert IsAdminCreateIsAuthenticatedRead().has_permission(mocked_request, None)

    mocked_request.method = "DELETE"
    assert IsAdminCreateIsAuthenticatedRead().has_permission(mocked_request, None)

    mocked_request.method = "GET"
    assert IsAdminCreateIsAuthenticatedRead().has_permission(mocked_request, None)


@pytest.mark.django_db
@patch("django.http.request.HttpRequest")
def test_permission_for_admin(mocked_request, base_user):
    mocked_request.method = "POST"
    mocked_request.user = base_user
    assert not IsAdminCreateIsAuthenticatedRead().has_permission(mocked_request, None)

    mocked_request.method = "PUT"
    assert not IsAdminCreateIsAuthenticatedRead().has_permission(mocked_request, None)

    mocked_request.method = "DELETE"
    assert not IsAdminCreateIsAuthenticatedRead().has_permission(mocked_request, None)

    mocked_request.method = "GET"
    assert IsAdminCreateIsAuthenticatedRead().has_permission(mocked_request, None)

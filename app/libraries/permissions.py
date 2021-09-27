from rest_framework.permissions import BasePermission


class IsAdminCreateIsAuthenticatedRead(BasePermission):
    """
    Create and update allowed only to admin users. Reade  allowed only authenticated user.
    """

    def has_permission(self, request, view):
        if request.method in ("POST", "PUT", "DELETE", "PATCH"):
            return request.user and request.user.is_staff
        else:
            return request.user and request.user.is_authenticated

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    The request is authenticated as a owner, or is a read-only request.
    """

    def has_permission(self, request, view):
        try:
            allowed = request.user.id == view.get(request).data['author']
        except Exception as e:
            allowed = e and False
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            allowed
        )

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение.
    Позволяет только владельцам поста редактировать его.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

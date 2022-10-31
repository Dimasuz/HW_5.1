
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user and request.user.is_authenticated:
            return obj.creator == request.user or request.user.is_staff
        else:
            return False

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, course):
        if request.method in SAFE_METHODS:
            return True
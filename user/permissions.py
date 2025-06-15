from rest_framework import permissions

class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admin users can access any user
        if request.user.is_staff:
            return True
        # Users can only access their own profile
        return obj == request.user
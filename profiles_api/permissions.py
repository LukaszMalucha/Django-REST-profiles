from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        ## if user only view the profile
        if request.method in permissions.SAFE_METHODS:
            return True

        ## if user is trying to modify profile
        return obj.id == request.user.id
        ## If returned false, permission denied


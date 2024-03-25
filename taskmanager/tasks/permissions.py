from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners or admins to edit or delete an object.
    """
    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner or admin
        return obj.owner == request.user or request.user.is_superuser


class IsSuperUserOrAssignedUser(permissions.BasePermission):
    """
    Custom permission to allow superuser to see all tasks and assigned users to see their tasks.
    """
    def has_object_permission(self, request, view, obj):
        # Superusers can see all tasks, regular users can only see their own tasks
        return request.user.is_superuser or obj.owner == request.user

    def has_permission(self, request, view):
        # Superusers can manipulate all tasks, regular users can only manipulate their own tasks
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        else:
            return False
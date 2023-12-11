from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS


class IsCreatorOrReadOnly(BasePermission):
    """Custom permission to only allow creator of an object to edit it."""
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.creator == request.user


class IsCreatorJobOrganizationOrReadonly(BasePermission):
    """
    Custom permission to only allow creator of an organization,
    which publish job to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.organization.creator == request.user


class IsAdminUserOrReadonly(IsAdminUser):
    """Custom permission to only allow admin users to edit it."""
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

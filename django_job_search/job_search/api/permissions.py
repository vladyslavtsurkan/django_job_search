from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS


class IsCreatorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.creator == request.user


class IsCreatorJobOrganizationOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.organization.creator == request.user


class IsAdminUserOrReadonly(IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

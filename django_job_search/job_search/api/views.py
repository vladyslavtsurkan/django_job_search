"""
This module contains the views for the API.
"""
# Required Django and Rest Framework imports
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin

# Local imports for filters, pagination, permissions and serializers
from job_search.api.filters import JobFilter
from job_search.api.pagination import JobResultsPagePagination, LocationResultsPagePagination
from job_search.api.permissions import (
    IsCreatorOrReadOnly,
    IsCreatorJobOrganizationOrReadonly,
    IsAdminUserOrReadonly,
)
from job_search.api.serializers import (
    DegreeSerializer,
    LocationSerializer,
    OrganizationSerializer,
    JobDetailSerializer,
    JobSerializer,
    SpotlightSerializer,
)
from job_search.models import Degree, Location, Organization, Job, Spotlight


class SpotlightViewSet(ModelViewSet):
    """
    ViewSet for Spotlight model.
    Only admin users can perform CRUD operations.
    The results are cached for 300 seconds.
    """
    queryset = Spotlight.objects.all()
    serializer_class = SpotlightSerializer
    permission_classes = [IsAdminUserOrReadonly]

    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        """
        List all the Spotlights.
        """
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific Spotlight.
        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """For admins. Create a new Spotlight."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """For admins. Update a specific Spotlight."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """For admins. Partially update a specific Spotlight."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """For admins. Delete a specific Spotlight."""
        return super().destroy(request, *args, **kwargs)


class DegreeViewSet(ModelViewSet):
    """
    ViewSet for Degree model.
    Only admin users can perform CRUD operations.
    The results are cached for 300 seconds.
    """
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [IsAdminUserOrReadonly]

    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        """
        List all the Degrees.
        """
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a specific Degree."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """For admins. Create a new Degree."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """For admins. Update a specific Degree."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """For admins. Partially update a specific Degree."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """For admins. Delete a specific Degree."""
        return super().destroy(request, *args, **kwargs)


class LocationViewSet(ListModelMixin, GenericViewSet):
    """
    ViewSet for Location model.
    Only supports listing of Locations.
    The results are paginated and cached for 120 seconds.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = LocationResultsPagePagination

    @method_decorator(cache_page(120))
    def list(self, request, *args, **kwargs):
        """List all the Locations."""
        return super().list(request, *args, **kwargs)


class OrganizationViewSet(ModelViewSet):
    """
    ViewSet for Organization model.
    Only authenticated users can perform CRUD operations.
    The results are cached for 120 seconds.
    """
    queryset = Organization.objects.select_related('creator')
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsCreatorOrReadOnly]

    def perform_create(self, serializer):
        """
        Save the creator of the Organization during creation.
        """
        serializer.save(creator=self.request.user)

    @method_decorator(cache_page(120))
    def list(self, request, *args, **kwargs):
        """List all the Organizations."""
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(120))
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a specific Organization."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Create a new Organization."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update a specific Organization."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partially update a specific Organization."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a specific Organization."""
        return super().destroy(request, *args, **kwargs)


class JobViewSet(ModelViewSet):
    """
    ViewSet for Job model.
    Only authenticated users can perform CRUD operations.
    The results are paginated and cached for 120 seconds.
    """
    queryset = Job.objects.all()
    filterset_class = JobFilter
    pagination_class = JobResultsPagePagination
    permission_classes = [IsAuthenticatedOrReadOnly & IsCreatorJobOrganizationOrReadonly]

    def get_serializer_class(self):
        """
        Use different serializers for list and detail views.
        """
        if self.action == 'list':
            return JobSerializer
        return JobDetailSerializer

    def get_queryset(self):
        """
        Use different querysets for list and detail views.
        """
        if self.action in ('retrieve', 'create', 'update', 'partial_update'):
            return self.queryset.all().select_related(
                'degree', 'organization',
            ).prefetch_related('locations')

        return self.queryset.all().select_related(
            'degree', 'organization',
        ).prefetch_related('locations').only(
            'title', 'degree', 'locations', 'organization', 'minimum_qualifications',
            'job_type', 'date_added'
        )

    @method_decorator(cache_page(120))
    def list(self, request, *args, **kwargs):
        """List all the Jobs."""
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(120))
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a specific Job."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create a new Job. You can use only organization, which you created before.
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update a specific Job."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partially update a specific Job."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a specific Job."""
        return super().destroy(request, *args, **kwargs)

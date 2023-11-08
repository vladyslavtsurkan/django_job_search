from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from job_search.api.filters import JobFilter
from job_search.api.pagination import JobResultsPagePagination
from job_search.api.permissions import IsCreatorOrReadOnly, IsCreatorJobOrganizationOrReadonly, IsAdminUserOrReadonly
from job_search.api.serializers import (
    DegreeSerializer,
    LocationSerializer,
    OrganizationSerializer,
    JobDetailSerializer,
    JobSerializer,
    SpotlightSerializer
)
from job_search.models import Degree, Location, Organization, Job, Spotlight


class SpotlightViewSet(ModelViewSet):
    queryset = Spotlight.objects.all()
    serializer_class = SpotlightSerializer
    permission_classes = [IsAdminUserOrReadonly]

    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class DegreeViewSet(ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [IsAdminUserOrReadonly]

    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @method_decorator(cache_page(120))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(120))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.select_related('creator')
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsCreatorOrReadOnly]  # | IsAdminUser

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @method_decorator(cache_page(120))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(120))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    filterset_class = JobFilter
    pagination_class = JobResultsPagePagination
    permission_classes = [IsAuthenticatedOrReadOnly & IsCreatorJobOrganizationOrReadonly]

    def get_serializer_class(self):
        if self.action == 'list':
            return JobSerializer
        return JobDetailSerializer

    def get_queryset(self):
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
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(120))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

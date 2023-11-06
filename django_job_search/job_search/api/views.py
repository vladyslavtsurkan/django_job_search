from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from job_search.models import Degree, Location, Organization, Job, Spotlight
from job_search.api.serializers import (
    DegreeSerializer,
    LocationSerializer,
    OrganizationSerializer,
    JobDetailSerializer,
    JobSerializer,
    SpotlightSerializer
)
from job_search.api.filters import JobFilter


class SpotlightViewSet(ReadOnlyModelViewSet):
    queryset = Spotlight.objects.all()
    serializer_class = SpotlightSerializer

    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class DegreeViewSet(ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer

    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    filterset_class = JobFilter

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return JobSerializer
        return JobDetailSerializer

    def get_queryset(self):
        if self.action not in ('list', 'create'):
            return self.queryset.all().select_related(
                'degree', 'organization'
            ).prefetch_related('locations')

        return self.queryset.all().select_related(
            'degree', 'organization'
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

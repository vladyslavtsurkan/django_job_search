from rest_framework.viewsets import ModelViewSet

from job_search.models import Degree, Location, Organization, Job, Spotlight
from job_search.api.serializers import (
    DegreeSerializer,
    LocationSerializer,
    OrganizationSerializer,
    JobSerializer,
    SpotlightSerializer
)


class SpotlightViewSet(ModelViewSet):
    queryset = Spotlight.objects.all()
    serializer_class = SpotlightSerializer


class DegreeViewSet(ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

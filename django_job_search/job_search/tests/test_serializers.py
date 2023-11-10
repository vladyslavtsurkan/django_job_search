from django.test import TestCase

from job_search.api.serializers import (
    JobSerializer,
    LocationSerializer,
    OrganizationSerializer,
    DegreeSerializer,
    SpotlightSerializer,
)
from job_search.models import Organization, Location, Degree
from accounts.models import CustomUser


class SerializerTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='Hjsajk141'
        )

    def test_spotlight_serializer(self):
        data = {
            'title': 'Test Spotlight',
            'img': 'http://example.com/image.jpg',
            'description': 'Test Description'
        }
        serializer = SpotlightSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_degree_serializer(self):
        data = {'name': 'Test Degree'}
        serializer = DegreeSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_organization_serializer(self):
        data = {'name': 'Test Organization'}
        serializer = OrganizationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        # Test creator field read-only
        serializer.validated_data['creator'] = self.user
        instance = serializer.save()
        self.assertEqual(instance.creator, self.user)

    def test_location_serializer(self):
        data = {'name': 'Test Location'}
        serializer = LocationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_job_serializer(self):
        degree = Degree.objects.create(name='Test Degree')
        organization = Organization.objects.create(name='Test Organization', creator=self.user)
        location = Location.objects.create(name='Test Location')

        data = {
            'title': 'Test Job',
            'degree': degree.name,
            'organization': organization.name,
            'locations': [location.name],
            'minimum_qualifications': ['Test Qualification'],
            'job_type': 'Full-time'
        }

        serializer = JobSerializer(data=data)
        self.assertTrue(serializer.is_valid())

from django.test import TestCase

from job_search.api.serializers import JobSerializer
from job_search.models import Organization, Location, Degree
from accounts.models import CustomUser


class SerializersTestCase(TestCase):
    def test_job_serializer(self):
        degree = Degree.objects.create(name='Test Degree')
        user = CustomUser.objects.create_user(email='test@example.com', password='Hjsajk141')
        organization = Organization.objects.create(name='Test Organization', creator=user)
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

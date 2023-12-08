from django.test import TestCase
from django.contrib.auth import get_user_model

from job_search.models import Spotlight, Degree, Organization, Location, Job


class ModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com', password='Hjsajk141'
        )
        self.degree = Degree.objects.create(name='Test Degree 2')
        self.organization = Organization.objects.create(
            name='Test Organization 2', creator=self.user
        )
        self.location = Location.objects.create(name='Test Location 2')

    def test_spotlight_creation_is_successful(self):
        title = 'Test Spotlight'
        img = 'http://test.com'
        description = 'Test Description'
        spotlight = Spotlight.objects.create(title=title, img=img, description=description)
        self.assertTrue(isinstance(spotlight, Spotlight))
        self.assertEqual(title, spotlight.title)
        self.assertEqual(img, spotlight.img)
        self.assertEqual(description, spotlight.description)

    def test_degree_creation_is_successful(self):
        name = 'Test Degree'
        degree = Degree.objects.create(name=name)
        self.assertTrue(isinstance(degree, Degree))
        self.assertEqual(name, degree.name)

    def test_organization_creation_is_successful(self):
        name = 'Test Organization'
        organization = Organization.objects.create(name=name, creator=self.user)
        self.assertTrue(isinstance(organization, Organization))
        self.assertEqual(name, organization.name)

    def test_location_creation_is_successful(self):
        name = 'Test Location'
        location = Location.objects.create(name=name)
        self.assertTrue(isinstance(location, Location))
        self.assertEqual(name, location.name)

    def test_job_creation_is_successful(self):
        job = Job.objects.create(
            title='Test Job',
            degree=self.degree,
            organization=self.organization,
            preferred_qualifications=['Test Qualification'],
            minimum_qualifications=['Test Qualification'],
            description=['Test Description'],
            job_type='Full-time'
        )
        job.locations.set([self.location])
        self.assertTrue(isinstance(job, Job))

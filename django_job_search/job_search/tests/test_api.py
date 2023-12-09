from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from job_search.models import Degree, Location, Organization, Job, Spotlight


class SpotlightViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.spotlight = Spotlight.objects.create(
            title='Test Spotlight',
            img='https://example.com/test.jpg',
            description='Test Description'
        )

    def test_list_spotlights(self):
        response = self.client.get(reverse('job_search:spotlight-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_spotlight(self):
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DegreeViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.degree = Degree.objects.create(name='Test Degree')

    def test_list_degrees(self):
        response = self.client.get(reverse('job_search:degree-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_degree(self):
        response = self.client.get(reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LocationViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.location = Location.objects.create(name='Test Location')

    def test_list_locations(self):
        response = self.client.get(reverse('job_search:location-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_location(self):
        response = self.client.get(reverse('job_search:location-detail', kwargs={'pk': self.location.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrganizationViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(email='test@example.com', password='Hkfsfkdj!23')
        self.organization = Organization.objects.create(name='Test Organization', creator=self.user)

    def test_list_organizations(self):
        response = self.client.get(reverse('job_search:organization-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_organization(self):
        response = self.client.get(
            reverse('job_search:organization-detail', kwargs={'pk': self.organization.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class JobViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(email='test@example.com', password='Hkfsfkdj!23')
        self.organization = Organization.objects.create(name='Test Organization', creator=self.user)
        self.degree = Degree.objects.create(name='Test Degree')
        self.location = Location.objects.create(name='Test Location')
        self.job = Job.objects.create(
            title='Test Job',
            organization=self.organization,
            degree=self.degree,
            minimum_qualifications=['Test Qualification'],
            job_type='Full-time',
            preferred_qualifications=['Test Qualification'],
            description=['Test Description'],
        )

    def test_list_jobs(self):
        response = self.client.get(reverse('job_search:job-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_job(self):
        response = self.client.get(reverse('job_search:job-detail', kwargs={'pk': self.job.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

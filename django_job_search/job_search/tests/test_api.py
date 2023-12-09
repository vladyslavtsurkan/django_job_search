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
        self.superuser = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='Hkfsfkdj!23'
        )
        self.user = get_user_model().objects.create_user(
            email='test2@example.com',
            password='Hkfsfkdj!23'
        )

    def force_authenticate_superuser(self):
        self.client.force_authenticate(user=self.superuser)

    def force_authenticate_user(self):
        self.client.force_authenticate(user=self.user)

    def test_list_spotlights(self):
        response = self.client.get(reverse('job_search:spotlight-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_spotlight(self):
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_spotlight_as_superuser(self):
        self.force_authenticate_superuser()
        data = {
            'title': 'Test Spotlight 2',
            'img': 'https://example.com/test.jpg',
            'description': 'Test Description'
        }
        response = self.client.post(reverse('job_search:spotlight-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_spotlight_as_user(self):
        self.force_authenticate_user()
        data = {
            'title': 'Test Spotlight 2',
            'img': 'https://example.com/test.jpg',
            'description': 'Test Description'
        }
        response = self.client.post(reverse('job_search:spotlight-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_spotlight_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'title': 'Test Spotlight 2',
            'img': 'https://example.com/test.jpg',
            'description': 'Test Description'
        }
        response = self.client.post(reverse('job_search:spotlight-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_spotlight_as_superuser(self):
        self.force_authenticate_superuser()
        data = {
            'title': 'Test Spotlight 2',
            'img': 'https://example.com/test.jpg',
            'description': 'Test Description'
        }
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_spotlight_as_user(self):
        self.force_authenticate_user()
        data = {
            'title': 'Test Spotlight 2',
            'img': 'https://example.com/test.jpg',
            'description': 'Test Description'
        }
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_spotlight_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'title': 'Test Spotlight 2',
            'img': 'https://example.com/test.jpg',
            'description': 'Test Description'
        }
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update_spotlight_as_superuser(self):
        self.force_authenticate_superuser()
        data = {
            'title': 'Test Spotlight 2',
        }
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_spotlight_as_user(self):
        self.force_authenticate_user()
        data = {
            'title': 'Test Spotlight 2',
        }
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_spotlight_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'title': 'Test Spotlight 2',
        }
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_spotlight_as_superuser(self):
        self.force_authenticate_superuser()
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_spotlight_as_user(self):
        self.force_authenticate_user()
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_spotlight_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('job_search:spotlight-detail', kwargs={'pk': self.spotlight.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class DegreeViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.degree = Degree.objects.create(name='Test Degree')
        self.superuser = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='Hkfsfkdj!23'
        )
        self.user = get_user_model().objects.create_user(
            email='test2@example.com',
            password='Hkfsfkdj!23'
        )

    def force_authenticate_superuser(self):
        self.client.force_authenticate(user=self.superuser)

    def force_authenticate_user(self):
        self.client.force_authenticate(user=self.user)

    def test_list_degrees(self):
        response = self.client.get(reverse('job_search:degree-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_degree(self):
        response = self.client.get(reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_degree_as_superuser(self):
        self.force_authenticate_superuser()
        data = {
            'name': 'Test Degree 2'
        }
        response = self.client.post(reverse('job_search:degree-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_degree_as_user(self):
        self.force_authenticate_user()
        data = {
            'name': 'Test Degree 2'
        }
        response = self.client.post(reverse('job_search:degree-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_degree_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'name': 'Test Degree 2'
        }
        response = self.client.post(reverse('job_search:degree-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_degree_as_superuser(self):
        self.force_authenticate_superuser()
        data = {
            'name': 'Test Degree 2'
        }
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_degree_as_user(self):
        self.force_authenticate_user()
        data = {
            'name': 'Test Degree 2'
        }
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_degree_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'name': 'Test Degree 2'
        }
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update_degree_as_superuser(self):
        self.force_authenticate_superuser()
        data = {
            'name': 'Test Degree 2'
        }
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_degree_as_user(self):
        self.force_authenticate_user()
        data = {
            'name': 'Test Degree 2'
        }
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_degree_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'name': 'Test Degree 2'
        }
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_degree_as_superuser(self):
        self.force_authenticate_superuser()
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_degree_as_user(self):
        self.force_authenticate_user()
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_degree_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('job_search:degree-detail', kwargs={'pk': self.degree.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


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
        self.user1 = get_user_model().objects.create_user(email='test1@example.com', password='Hkfsfkdj!23')
        self.user2 = get_user_model().objects.create_user(email='test2@example.com', password='Hkfsfkdj!23')
        self.organization1 = Organization.objects.create(name='Test Organization', creator=self.user1)
        self.organization2 = Organization.objects.create(name='Test Organization 2', creator=self.user2)

    def test_list_organizations(self):
        response = self.client.get(reverse('job_search:organization-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_organization(self):
        response = self.client.get(
            reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_organization_as_user(self):
        self.client.force_authenticate(user=self.user1)
        data = {
            'name': 'Test Organization 3'
        }
        response = self.client.post(reverse('job_search:organization-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_organization_as_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'name': 'Test Organization 3'
        }
        response = self.client.post(reverse('job_search:organization-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_organization_as_creator(self):
        self.client.force_authenticate(user=self.user1)
        data = {
            'name': 'Test Organization 4'
        }
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_organization_as_non_creator(self):
        self.client.force_authenticate(user=self.user2)
        data = {
            'name': 'Test Organization 4'
        }
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_organization_as_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'name': 'Test Organization 4'
        }
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update_organization_as_creator(self):
        self.client.force_authenticate(user=self.user1)
        data = {
            'name': 'Test Organization 4'
        }
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_organization_as_non_creator(self):
        self.client.force_authenticate(user=self.user2)
        data = {
            'name': 'Test Organization 4'
        }
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_organization_as_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'name': 'Test Organization 4'
        }
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_organization_as_creator(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_organization_as_non_creator(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_organization_as_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('job_search:organization-detail', kwargs={'pk': self.organization1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class JobViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = get_user_model().objects.create_user(email='test1@example.com', password='Hkfsfkdj!23')
        self.user2 = get_user_model().objects.create_user(email='test2@example.com', password='Hkfsfkdj!23')
        self.organization1 = Organization.objects.create(name='Test Organization', creator=self.user1)
        self.organization2 = Organization.objects.create(name='Test Organization 2', creator=self.user2)
        self.degree = Degree.objects.create(name='Test Degree')
        self.location = Location.objects.create(name='Test Location')
        self.job = Job.objects.create(
            title='Test Job',
            organization=self.organization1,
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

    def test_create_job_as_creator_of_organization(self):
        self.client.force_authenticate(user=self.user1)
        data = {
            'title': 'Test Job 2',
            'organization': self.organization1.name,
            'degree': self.degree.name,
            'minimum_qualifications': ['Test Qualification'],
            'job_type': 'Full-time',
            'preferred_qualifications': ['Test Qualification'],
            'description': ['Test Description'],
        }
        response = self.client.post(reverse('job_search:job-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_job_as_non_creator_of_organization(self):
        self.client.force_authenticate(user=self.user2)
        data = {
            'title': 'Test Job 2',
            'organization': self.organization1.name,
            'degree': self.degree.name,
            'minimum_qualifications': ['Test Qualification'],
            'job_type': 'Full-time',
            'preferred_qualifications': ['Test Qualification'],
            'description': ['Test Description'],
        }
        response = self.client.post(reverse('job_search:job-list'), data=data)
        print(f'AAAAAAAAAAAAAAAA: {response.data}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_job_as_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'title': 'Test Job 2',
            'organization': self.organization1.name,
            'degree': self.degree.name,
            'minimum_qualifications': ['Test Qualification'],
            'job_type': 'Full-time',
            'preferred_qualifications': ['Test Qualification'],
            'description': ['Test Description'],
        }
        response = self.client.post(reverse('job_search:job-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_job_as_creator_of_organization(self):
        self.client.force_authenticate(user=self.user1)
        data = {
            'title': 'Test Job 2',
            'organization': self.organization1.name,
            'degree': self.degree.name,
            'minimum_qualifications': ['Test Qualification'],
            'job_type': 'Full-time',
            'preferred_qualifications': ['Test Qualification'],
            'description': ['Test Description'],
        }
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_job_as_non_creator_of_organization(self):
        self.client.force_authenticate(user=self.user2)
        data = {
            'title': 'Test Job 2',
            'organization': self.organization1.name,
            'degree': self.degree.name,
            'minimum_qualifications': ['Test Qualification'],
            'job_type': 'Full-time',
            'preferred_qualifications': ['Test Qualification'],
            'description': ['Test Description'],
        }
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_job_as_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'title': 'Test Job 2',
            'organization': self.organization1.name,
            'degree': self.degree.name,
            'minimum_qualifications': ['Test Qualification'],
            'job_type': 'Full-time',
            'preferred_qualifications': ['Test Qualification'],
            'description': ['Test Description'],
        }
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update_job_as_creator_of_organization(self):
        self.client.force_authenticate(user=self.user1)
        data = {
            'title': 'Test Job 2',
        }
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_job_as_non_creator_of_organization(self):
        self.client.force_authenticate(user=self.user2)
        data = {
            'title': 'Test Job 2',
        }
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_job_as_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'title': 'Test Job 2',
        }
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_job_as_creator_of_organization(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_job_as_non_creator_of_organization(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_job_as_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('job_search:job-detail', kwargs={'pk': self.job.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class JobSearchURLsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_urls_are_correctly_configured(self):
        response = self.client.get(reverse('job_search:search:job-list'))
        self.assertEqual(response.status_code, 200)

    def test_urls_handle_nonexistent_endpoints(self):
        response = self.client.get('/search/nonexistent/')
        self.assertEqual(response.status_code, 404)
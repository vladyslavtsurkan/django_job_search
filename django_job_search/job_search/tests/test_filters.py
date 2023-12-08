from django.test import TestCase
from django.contrib.auth import get_user_model

from job_search.models import Job, Organization, Degree
from job_search.api.filters import JobFilter


class JobFilterTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(email='test@example.com', password='Hdsjsjd1232')
        org = Organization.objects.create(name='Microsoft', creator=user)
        degree = Degree.objects.create(name='Bachelor')
        Job.objects.create(
            title='Software Engineer',
            organization=org,
            degree=degree,
            preferred_qualifications=['Python', 'Django', 'Django REST Framework'],
            minimum_qualifications=['Python', 'Django', 'Django REST Framework'],
            description=['Python', 'Django', 'Django REST Framework'],
        )

    def test_filter_by_exact_organization_name(self):
        f = JobFilter({'organization': 'Microsoft'}, queryset=Job.objects.all())
        self.assertEqual(len(f.qs), 1)

    def test_filter_by_exact_degree_name(self):
        f = JobFilter({'degree': 'Bachelor'}, queryset=Job.objects.all())
        self.assertEqual(len(f.qs), 1)

    def test_filter_by_non_existent_organization(self):
        f = JobFilter({'organization': 'Google'}, queryset=Job.objects.all())
        self.assertEqual(len(f.qs), 0)

    def test_filter_by_non_existent_degree(self):
        f = JobFilter({'degree': 'Master'}, queryset=Job.objects.all())
        self.assertEqual(len(f.qs), 0)

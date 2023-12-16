from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "test@example.com",
            "password": "TestPassword123",
        }

    def test_user_creation_is_successful(self):
        response = self.client.post(reverse('job_search:accounts:create'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().email, self.user_data["email"])

    def test_user_creation_fails_with_existing_email(self):
        test_data = {
            **self.user_data,
            "email": "test2@example.com",
        }
        get_user_model().objects.create_user(**test_data)
        response = self.client.post(reverse('job_search:accounts:create'), test_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AuthTokenAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "test@le.com",
            "password": "TestPassword123",
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_token_obtaining_is_successful(self):
        response = self.client.post(reverse('job_search:accounts:token'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_token_obtaining_fails_with_wrong_password(self):
        test_data = {
            **self.user_data,
            "password": "wrongpassword",
        }
        response = self.client.post(reverse('job_search:accounts:token'), test_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ManageUserAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "test@e.com",
            "password": "TestPassword123",
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_user_retrieval_is_successful(self):
        response = self.client.get(reverse('job_search:accounts:me'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user_data["email"])

    def test_user_update_is_successful(self):
        update_data = {"firstName": "Updated", "lastName": "User"}
        response = self.client.patch(reverse('job_search:accounts:me'), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data["first_name"], update_data["firstName"])
        self.assertEqual(response.data["last_name"], update_data["lastName"])

    def test_user_update_fails_without_authentication(self):
        self.client.force_authenticate(user=None)
        update_data = {"firstName": "Updated", "lastName": "User"}
        response = self.client.patch(reverse('job_search:accounts:me'), update_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

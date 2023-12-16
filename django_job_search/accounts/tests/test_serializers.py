from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from accounts.api.serializers import UserSerializer, AuthTokenSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "Test",
            "last_name": "User",
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_serializer_creates_user_correctly(self):
        test_data = {
            **self.user_data,
            "email": "test2@example.com",
        }
        serializer = UserSerializer(data=test_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, test_data["email"])
        self.assertTrue(user.check_password(test_data["password"]))
        self.assertEqual(user.first_name, test_data["first_name"])
        self.assertEqual(user.last_name, test_data["last_name"])

    def test_serializer_updates_user_correctly(self):
        update_data = {"first_name": "Updated", "last_name": "User"}
        serializer = UserSerializer(instance=self.user, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.first_name, update_data["first_name"])
        self.assertEqual(user.last_name, update_data["last_name"])


class AuthTokenSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "testpassword",
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_serializer_authenticates_user_correctly(self):
        serializer = AuthTokenSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["user"], self.user)

    def test_serializer_raises_error_for_invalid_credentials(self):
        invalid_data = {"email": "test@example.com", "password": "wrongpassword"}
        serializer = AuthTokenSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

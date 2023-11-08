from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = "test@example.com"
        password = "Test12398"

        user = get_user_model().objects.create_user(
            email,
            password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff and user.is_superuser)

    def test_create_superuser_with_email_successful(self):
        """Test creating a superuser with an email is successful."""
        email = "test@example.com"
        password = "Test12398"

        user = get_user_model().objects.create_superuser(
            email,
            password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff and user.is_superuser)

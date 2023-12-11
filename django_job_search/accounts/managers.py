from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    """
    Custom User Manager class that extends Django's UserManager.
    This class overrides the _create_user, create_user and create_superuser methods.
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Private method to create and save a User with the given email and password.

        Args:
            email (str): The email of the User.
            password (str): The password for the User.
            **extra_fields: Extra fields to be added to the User model.

        Raises:
            ValueError: If the email field is not set.

        Returns:
            User: The created User object.
        """
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Method to create a regular User.

        Args:
            email (str): The email of the User.
            password (str): The password for the User.
            **extra_fields: Extra fields to be added to the User model.

        Returns:
            User: The created User object.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Method to create a Superuser.

        Args:
            email (str): The email of the User.
            password (str): The password for the User.
            **extra_fields: Extra fields to be added to the User model.

        Raises:
            ValueError: If the is_staff or is_superuser field is not set to True.

        Returns:
            User: The created User object.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom User model that extends Django's AbstractUser.
    This model uses email as the USERNAME_FIELD and has no REQUIRED_FIELDS.

    Attributes:
        username (None): This field is set to None as we are using email as the username field.
        email (EmailField): This field stores the email of the user. It is unique and required.
        objects (CustomUserManager): This is the manager for the CustomUser model.
    """

    username = None
    email = models.EmailField(
        _("email address"),
        unique=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Method that returns a string representation of the CustomUser instance.

        Returns:
            str: The email of the user.
        """
        return self.email
    
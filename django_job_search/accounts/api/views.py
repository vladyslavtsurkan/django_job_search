"""
Views for the accounts app API.
"""
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, authentication
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.api.serializers import UserSerializer, AuthTokenSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """View to create a new user."""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class AuthTokenAPIView(ObtainAuthToken):
    """View to obtain a token for API authentication."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserAPIView(generics.RetrieveUpdateAPIView):
    """View to manage an existing user."""
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Method that returns the user object.

        Returns:
            User: The user object.
        """
        return self.request.user

"""
URL patterns for the accounts API
"""
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from accounts.api.views import UserCreateAPIView, AuthTokenAPIView, ManageUserAPIView

app_name = 'accounts'
urlpatterns = [
    # URLs for JWT authentication
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),

    # URL for creating a new user
    path('create/', UserCreateAPIView.as_view(), name='create'),

    # URL for obtaining a token for API authentication
    path('token/', AuthTokenAPIView.as_view(), name='token'),

    # URL for managing an authenticated user
    path('me/', ManageUserAPIView.as_view(), name='me'),
]

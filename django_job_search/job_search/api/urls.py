"""
This module defines the URLs for the Job Search API.

The API uses Django Rest Framework and includes JWT authentication.
It also includes auto-generated API documentation using drf-yasg.
"""
# Required Django and Rest Framework imports
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

# drf_yasg is used for auto-generating API documentation
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Local imports for the API views
from job_search.api.views import (
    OrganizationViewSet,
    DegreeViewSet,
    LocationViewSet,
    JobViewSet,
    SpotlightViewSet,
)

# Configure the schema view for drf_yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Job Search API",
        default_version="v1",
        description="API for Job Search website",
    ),
    url=f"http://127.0.0.1:8000/api/v1/",
    public=True,
)

# Create a default router and register the viewsets
router = DefaultRouter()
router.register('organizations', OrganizationViewSet)
router.register('degrees', DegreeViewSet)
router.register('locations', LocationViewSet)
router.register('jobs', JobViewSet)
router.register('spotlights', SpotlightViewSet)

# Define the URL patterns
urlpatterns = [
    # Include the default router URLs
    path('', include(router.urls)),

    # Include the accounts URLs
    path('accounts/', include('accounts.api.urls')),

    # Include the search URLs
    path('search/', include('search.urls')),

    # URLs for the API documentation in JSON and YAML formats
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),

    # URL for the Swagger UI
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    # URL for the Redoc UI
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc-ui",
    ),
]

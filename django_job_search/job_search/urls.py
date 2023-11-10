from django.urls import path, include

app_name = 'job_search'
urlpatterns = [
    path("api/v1/", include('job_search.api.urls')),
]

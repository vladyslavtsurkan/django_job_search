from django.urls import path, include
from rest_framework.routers import SimpleRouter

from search.views import JobDocumentViewSet

router = SimpleRouter()
router.register('jobs', JobDocumentViewSet, basename='job')

app_name = 'search'
urlpatterns = [
    path('', include(router.urls)),
]

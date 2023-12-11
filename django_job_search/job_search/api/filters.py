from django_filters import rest_framework as filters

from job_search.models import Job


class JobFilter(filters.FilterSet):
    """Filter for Job model."""
    title = filters.CharFilter(lookup_expr='icontains')
    organization = filters.CharFilter(lookup_expr='iexact', field_name='organization__name')
    degree = filters.CharFilter(lookup_expr='iexact', field_name='degree__name')

    class Meta:
        model = Job
        fields = ['locations', 'job_type']

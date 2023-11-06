from django_filters import rest_framework as filters

from job_search.models import Job


class JobFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['degree', 'locations', 'organization', 'job_type']

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    SearchFilterBackend,
    FilteringFilterBackend,
    SuggesterFilterBackend,
    FunctionalSuggesterFilterBackend,
)

from search.documents import JobDocument
from search.serializers import JobDocumentSerializer


class JobDocumentViewSet(DocumentViewSet):
    document = JobDocument
    serializer_class = JobDocumentSerializer

    filter_backends = [
        SearchFilterBackend,
        FilteringFilterBackend,
        SuggesterFilterBackend,
        FunctionalSuggesterFilterBackend,
    ]

    search_fields = (
        'job_title',
        'degree',
        'organization',
        'locations',
        'preferred_qualifications',
        'minimum_qualifications',
        'description',
        'job_type',
    )

    filter_fields = {
        'job_title': 'job_title',
        'degree': 'job_degree.name',
        'organization': 'job_organization.name',
        'locations': 'locations.name',
        'job_type': 'job_type',

    }

    suggester_fields = {
        'job_title_suggest': {
            'field': 'job_title.suggest',
            'suggesters': [
                'job_title_suggest',
                'job_title_suggest_context',
            ],
            'default_suggester': 'job_title_suggest',
        },
    }

    functional_suggester_fields = {
        'job_title_suggest': {
            'suggesters': [
                'job_title_suggest',
                'job_title_suggest_context',
            ],
            'default_suggester': 'job_title_suggest',
        },
    }

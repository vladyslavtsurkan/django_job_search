from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    SearchFilterBackend,
    FilteringFilterBackend,
    SuggesterFilterBackend,
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
    ]

    search_fields = (
        'job_title',
        'job_degree',
        'job_organization',
        'locations',
        'preferred_qualifications',
        'minimum_qualifications',
        'description',
        'job_type',
    )

    filter_fields = {
        'id': None,
        'job_title': 'job_title.raw',
        'job_degree': 'job_degree.name.raw',
        'job_organization': 'job_organization.name.raw',
        'locations': 'locations.name.raw',
        'preferred_qualifications': 'preferred_qualifications.raw',
        'minimum_qualifications': 'minimum_qualifications.raw',
        'description': 'description.raw',
        'job_type': 'job_type.raw',
        'date_added': 'date_added',
        'date_updated': 'date_updated',
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

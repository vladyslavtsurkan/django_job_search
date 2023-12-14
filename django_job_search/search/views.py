from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    SearchFilterBackend,
    MultiMatchSearchFilterBackend,
    FilteringFilterBackend,
    SuggesterFilterBackend,
    FunctionalSuggesterFilterBackend,
    DefaultOrderingFilterBackend,
)

from search.documents import JobDocument
from search.serializers import JobDocumentSerializer


class JobDocumentViewSet(DocumentViewSet):
    document = JobDocument
    serializer_class = JobDocumentSerializer

    filter_backends = [
        SearchFilterBackend,
        MultiMatchSearchFilterBackend,
        FilteringFilterBackend,
        SuggesterFilterBackend,
        FunctionalSuggesterFilterBackend,
        DefaultOrderingFilterBackend,
    ]

    search_fields = {
        'job_title': {'fuzziness': 'AUTO'},
        'degree': None,
        'organization': {'fuzziness': 'AUTO'},
        'locations': None,
        'preferred_qualifications': None,
        'minimum_qualifications': None,
        'description': None,
        'job_type': None,
    }

    multi_match_search_fields = {
        'job_title': {'fuzziness': 'AUTO'},
        'degree': None,
        'organization': {'fuzziness': 'AUTO'},
        'locations': None,
        'preferred_qualifications': None,
        'minimum_qualifications': None,
        'description': None,
        'job_type': None,
    }

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

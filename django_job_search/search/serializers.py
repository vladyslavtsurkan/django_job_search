from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search.documents import JobDocument


class JobDocumentSerializer(DocumentSerializer):
    class Meta:
        document = JobDocument
        fields = (
            'id',
            'job_title',
            'job_degree',
            'job_organization',
            'locations',
            'preferred_qualifications',
            'minimum_qualifications',
            'description',
            'job_type',
            'date_added',
            'date_updated',
        )

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from search.documents import JobDocument


class JobDocumentSerializer(DocumentSerializer):
    title = serializers.CharField(source='job_title')
    degree = serializers.CharField(source='degree.name')
    organization = serializers.CharField(source='organization.name')
    locations = serializers.SerializerMethodField()

    def get_locations(self, obj):
        return [location.name for location in obj.locations]

    class Meta:
        document = JobDocument
        fields = (
            'id',
            'title',
            'degree',
            'organization',
            'locations',
            'preferred_qualifications',
            'minimum_qualifications',
            'description',
            'job_type',
            'date_added',
            'date_updated',
        )

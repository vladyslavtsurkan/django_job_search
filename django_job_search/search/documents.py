from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from job_search.models import Job


@registry.register_document
class JobDocument(Document):
    id = fields.IntegerField(attr='id')
    job_title = fields.TextField(
        attr='title',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.Completion(),
        }
    )
    degree = fields.ObjectField(
        attr='degree',
        properties={
            'id': fields.IntegerField(),
            'name': fields.TextField(),
        }
    )
    organization = fields.ObjectField(
        attr='organization',
        properties={
            'id': fields.IntegerField(),
            'name': fields.TextField(),
        }
    )

    locations = fields.NestedField(
        attr='locations',
        properties={
            'id': fields.IntegerField(),
            'name': fields.TextField(),
        }
    )

    preferred_qualifications = fields.ListField(fields.TextField())
    minimum_qualifications = fields.ListField(fields.TextField())
    description = fields.ListField(fields.TextField())

    job_type = fields.TextField(attr='job_type')

    date_added = fields.DateField(attr='date_added')
    date_updated = fields.DateField(attr='date_updated')

    class Index:
        name = 'jobs'

    class Django:
        model = Job
        fields = [
            'title',
        ]
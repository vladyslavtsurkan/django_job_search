from rest_framework.exceptions import ValidationError

from job_search.models import Organization


def job_serializer_save_or_raise_exception_by_organization(serializer, user):
    organization_name = serializer.validated_data.get('organization', None)

    if organization_name is not None:
        organization = Organization.objects.get(name=organization_name['name'])

        if organization.creator != user:
            raise ValidationError({'organization': ['Creator of this organization is not of current user.']})

    serializer.save()

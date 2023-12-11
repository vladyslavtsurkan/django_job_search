from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied

from job_search.api.fields import SlugRelatedCreationField
from job_search.models import Organization, Degree, Location, Job, Spotlight


class SpotlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spotlight
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source='creator.email', read_only=True)

    class Meta:
        model = Organization
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance.name

    class Meta:
        model = Location
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    locations = SlugRelatedCreationField(
        many=True,
        slug_field='name',
        queryset=Location.objects.all()
    )
    degree = serializers.CharField(source='degree.name')
    organization = serializers.CharField(source='organization.name')

    def validate_organization(self, value):
        try:
            organization = Organization.objects.get(name=value)
        except Organization.DoesNotExist:
            raise ValidationError(f'Object with name={value} does not exist.')

        request = self.context.get('request')
        if request is not None and organization.creator != request.user:
            raise PermissionDenied('Creator of this organization is not of current user.')

        return value

    def validate_degree(self, value):
        try:
            Degree.objects.get(name=value)
        except Degree.DoesNotExist:
            raise ValidationError(f'Object with name={value} does not exist.')

        return value

    def create(self, validated_data):
        degree_name = validated_data.pop('degree')['name']
        organization_name = validated_data.pop('organization')['name']

        validated_data['degree'] = Degree.objects.get(name=degree_name)
        validated_data['organization'] = Organization.objects.get(name=organization_name)
        location_names = validated_data.pop('locations')

        job = Job.objects.create(**validated_data)

        for location_name in location_names:
            location, _ = Location.objects.get_or_create(name=location_name)
            job.locations.add(location)

        return job

    def update(self, instance, validated_data):
        job = Job.objects.get(pk=instance.id)

        degree_data = validated_data.pop('degree', None)
        organization_data = validated_data.pop('organization', None)

        if degree_data is not None:
            degree_name = degree_data.get('name')
            degree = Degree.objects.get(name=degree_name)
            validated_data['degree'] = degree

        if organization_data is not None:
            organization_name = organization_data.get('name')
            organization = Organization.objects.get(name=organization_name)
            validated_data['organization'] = organization

        location_names = validated_data.pop('locations', None)

        if location_names is not None:
            locations = []
            for location_name in location_names:
                location, _ = Location.objects.get_or_create(name=location_name)
                locations.append(location)

            job.locations.set(locations)

        for attr, value in validated_data.items():
            setattr(job, attr, value)

        job.save()

        return job

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'degree',
            'locations',
            'organization',
            'minimum_qualifications',
            'job_type',
            'date_added'
        ]
        extra_kwargs = {'date_added': {'read_only': True}}


class JobDetailSerializer(JobSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        extra_kwargs = {
            'date_added': {'read_only': True},
            'date_updated': {'read_only': True},
        }


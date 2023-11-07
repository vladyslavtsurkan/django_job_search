from rest_framework import serializers

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
    class Meta:
        model = Location
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Location.objects.all()
    )
    degree = serializers.CharField(source='degree.name')
    organization = serializers.CharField(source='organization.name')

    def create(self, validated_data):
        degree_name = validated_data.pop('degree')['name']
        organization_name = validated_data.pop('organization')['name']

        degree = Degree.objects.get(name=degree_name)
        organization = Organization.objects.get(name=organization_name)
        location_names = validated_data.pop('locations')

        job = Job.objects.create(
            degree=degree,
            organization=organization,
            **validated_data
        )

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


class JobDetailSerializer(JobSerializer):
    class Meta:
        model = Job
        fields = '__all__'

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


class LocationNameSerializer(LocationSerializer):
    def to_representation(self, instance):
        return instance.name


class JobSerializer(serializers.ModelSerializer):
    locations = LocationNameSerializer(many=True)

    class Meta:
        model = Job
        fields = [
            'title',
            'degree',
            'locations',
            'organization',
            'minimum_qualifications',
            'job_type',
            'date_added'
        ]


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

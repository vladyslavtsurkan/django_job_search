import json

from django.core.management import BaseCommand

from job_search.models import Degree, Organization, Location, Spotlight, Job


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('db.json') as file:
            db_json = json.loads(file.read())

        degrees = db_json.get('degrees')
        spotlights = db_json.get('spotlights')
        jobs = db_json.get('jobs')

        for degree in degrees:
            Degree.objects.get_or_create(name=degree.get('degree', ''))

        for spotlight in spotlights:
            Spotlight.objects.get_or_create(
                title=spotlight.get('title'),
                img=spotlight.get('img'),
                description=spotlight.get('description')
            )

        for job in jobs:
            degree_instance = Degree.objects.get(name=job.get('degree'))
            organization_instance, created = Organization.objects.get_or_create(
                name=job.get('organization'),
                creator_id=1
            )

            job_instance, created = Job.objects.get_or_create(
                title=job.get('title'),
                organization=organization_instance,
                degree=degree_instance,
                job_type=job.get('jobType'),
                minimum_qualifications=job.get('minimumQualifications'),
                preferred_qualifications=job.get('preferredQualifications'),
                description=job.get('description'),
            )

            for location in job.get('locations'):
                location_instance, created = Location.objects.get_or_create(
                    name=location
                )
                job_instance.locations.add(location_instance)

            job_instance.save()

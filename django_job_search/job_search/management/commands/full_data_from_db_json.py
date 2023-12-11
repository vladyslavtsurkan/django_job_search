"""
This module defines a Django management command that populates the database from a JSON file.

The command reads data from a file named 'db.json' in the same directory.
It creates instances of the Degree, Spotlight, Job, Organization, and Location models.

The 'handle' method is the entry point for the command.
"""
import json

from django.core.management import BaseCommand

from job_search.models import Degree, Organization, Location, Spotlight, Job


class Command(BaseCommand):
    """
    Django management command to populate the database from a JSON file.
    """
    def handle(self, *args, **options):
        """
        Handle the command.

        Reads data from 'db.json' and creates instances of the
        Degree, Spotlight, Job, Organization, and Location models.
        """
        with open('db.json') as file:
            db_json = json.loads(file.read())

        degrees = db_json.get('degrees')
        spotlights = db_json.get('spotlights')
        jobs = db_json.get('jobs')

        # Create Degree instances
        for degree in degrees:
            Degree.objects.get_or_create(name=degree.get('degree', ''))

        # Create Spotlight instances
        for spotlight in spotlights:
            Spotlight.objects.get_or_create(
                title=spotlight.get('title'),
                img=spotlight.get('img'),
                description=spotlight.get('description')
            )

        # Create Job and related Organization and Location instances
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

            # Create Location instances and associate them with the Job instance
            for location in job.get('locations'):
                location_instance, created = Location.objects.get_or_create(
                    name=location
                )
                job_instance.locations.add(location_instance)

            job_instance.save()

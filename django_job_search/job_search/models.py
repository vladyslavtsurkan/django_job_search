from django.db import models

from django_jsonform.models.fields import ArrayField


class Spotlight(models.Model):
    title = models.CharField('Title', max_length=50)
    img = models.URLField('Image')
    description = models.TextField()

    def __str__(self):
        return self.title


class Degree(models.Model):
    name = models.CharField("Degree name", max_length=30, unique=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField("Organization name", unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField("Location name", unique=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField("Job title", max_length=100)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="jobs")
    locations = models.ManyToManyField(Location, related_name="jobs")

    preferred_qualifications = ArrayField(models.CharField(max_length=255))
    minimum_qualifications = ArrayField(models.CharField(max_length=255))
    description = ArrayField(models.CharField(max_length=255))

    job_type = models.CharField(
        "Job type",
        max_length=50,
        choices=[
            ("Full-time", "Full-time"),
            ("Part-time", "Part-time"),
            ("Intern", "Intern"),
            ("Temporary", "Temporary"),
        ],
    )

    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.organization.name}'

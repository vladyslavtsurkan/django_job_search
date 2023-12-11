"""
This module defines the models for the Job Search application.

The models include:
- Spotlight: Represents a spotlight item with a title, image, and description.
- Degree: Represents a degree with a unique name.
- Organization: Represents an organization with a unique name and a creator.
- Location: Represents a location with a unique name.
- Job: Represents a job with a title, associated degree, organization, and locations, 
  preferred and minimum qualifications, a description, job type, and dates when the job was added and updated.
"""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_jsonform.models.fields import ArrayField


class Spotlight(models.Model):
    """
    Spotlight model.
    Represents a spotlight item with a title, image, and description.
    """
    title = models.CharField(_('title'), max_length=50)
    img = models.URLField(_('image'))
    description = models.TextField(_('description'))

    class Meta:
        verbose_name = _('spotlight')
        verbose_name_plural = _('spotlights')

    def __str__(self):
        return self.title


class Degree(models.Model):
    """
    Degree model.
    Represents a degree with a unique name.
    """
    name = models.CharField(_("degree name"), max_length=30, unique=True)

    class Meta:
        verbose_name = _('degree')
        verbose_name_plural = _('degrees')

    def __str__(self):
        return self.name


class Organization(models.Model):
    """
    Organization model.
    Represents an organization with a unique name and a creator.
    """
    name = models.CharField(_("organization name"), unique=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organizations',
        null=False,
    )

    class Meta:
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    Location model.
    Represents a location with a unique name.
    """
    name = models.CharField(_("location name"), unique=True)

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')

    def __str__(self):
        return self.name


class Job(models.Model):
    """
    Job model.
    Represents a job with a title, associated degree, organization, and locations, 
    preferred and minimum qualifications, a description, job type, and dates when the job was added and updated.
    """
    title = models.CharField(_("job title"), max_length=100)

    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name="jobs")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="jobs")
    locations = models.ManyToManyField(Location, related_name="jobs")

    preferred_qualifications = ArrayField(models.CharField(max_length=255))
    minimum_qualifications = ArrayField(models.CharField(max_length=255))
    description = ArrayField(models.CharField(max_length=255))

    job_type = models.CharField(
        _("job type"),
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

    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')

    def __str__(self):
        return f'{self.title} by {self.organization.name}'

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_jsonform.models.fields import ArrayField


class Spotlight(models.Model):
    title = models.CharField(_('title'), max_length=50)
    img = models.URLField(_('image'))
    description = models.TextField(_('description'))

    class Meta:
        verbose_name = _('spotlight')
        verbose_name_plural = _('spotlights')

    def __str__(self):
        return self.title


class Degree(models.Model):
    name = models.CharField(_("degree name"), max_length=30, unique=True)

    class Meta:
        verbose_name = _('degree')
        verbose_name_plural = _('degrees')

    def __str__(self):
        return self.name


class Organization(models.Model):
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
    name = models.CharField(_("location name"), unique=True)

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')

    def __str__(self):
        return self.name


class Job(models.Model):
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

from django.contrib import admin

from job_search.models import Job, Location, Organization, Degree

admin.site.register(Job)
admin.site.register(Location)
admin.site.register(Organization)
admin.site.register(Degree)

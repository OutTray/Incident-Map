from django.db import models

# Create your models here.

class Incidents(models.Model):
    id = models.IntegerField(primary_key = True, blank=True)
    date_uploaded = models.CharField(max_length=255, blank=True, null=True)
    incident_date = models.IntegerField(blank=True, null=True)
    incident_time = models.CharField(max_length=255, blank=True, null=True)
    reported_date = models.CharField(max_length=255, blank=True, null=True)
    reported_time = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    incident_type = models.CharField(max_length=255, blank=True, null=True)
    hyperlinks = models.CharField(max_length=255, blank=True, null=True)
    incident_details = models.TextField(blank=True, null=True)
    suspect_descriptions = models.TextField(blank=True, null=True)
    top_pixels = models.IntegerField(blank=True, null=True)
    left_pixels = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidents'


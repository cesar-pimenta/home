from django.db import models

# Create your models here.

class EvenType(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)


class Event(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    type = models.ForeignKey(EvenType, blank=True, null=True, on_delete=models.CASCADE)
    date_ini = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
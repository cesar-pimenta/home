from django.db import models
from mission.models import Mission
from django.urls import reverse

# Create your models here.

class EvenType(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Tipo de Evento'
        verbose_name_plural = 'Tipos de Evento'

    def __str__(self):
        return '{}'.format(self.name)


class Event(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    tipe = models.ForeignKey(EvenType, blank=True, null=True, on_delete=models.CASCADE)
    date_ini = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    mission = models.ForeignKey(Mission, blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return '{}'.format(self.name)


    def get_absolute_url(self):
        return reverse('schedule:schedule_detail',
                       args=[self.id, self.slug])
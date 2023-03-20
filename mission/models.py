from django.db import models
from django.urls import reverse
from . import choices


class Mission(models.Model):    
    name = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date = models.CharField(max_length=10, choices=choices.DAYS_CHOICES, blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    status_missao = models.PositiveIntegerField(choices=choices.MISSAO_STATUS_CHOICES, default=0, blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Missão'
        verbose_name_plural = 'Missões'

    def __str__(self):
        return '{}'.format(self.name)
    

    def get_absolute_url(self):
        return reverse('mission:mission_detail',
                       args=[self.id, self.slug])
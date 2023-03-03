from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    apelido = models.CharField(max_length=250, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    resumo = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username}'


    def name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
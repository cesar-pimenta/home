# Generated by Django 4.1.7 on 2023-03-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mission',
            name='status_missao',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'criação'), (1, 'dicernimento'), (2, 'ativa'), (3, 'desativada')], default=0, null=True),
        ),
    ]

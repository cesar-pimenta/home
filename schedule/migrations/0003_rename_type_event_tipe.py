# Generated by Django 4.1.7 on 2023-03-22 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_event_mission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='type',
            new_name='tipe',
        ),
    ]

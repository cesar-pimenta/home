# Generated by Django 4.1.7 on 2023-03-22 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_rename_type_event_tipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-28 21:54

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-29 03:42

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_banner',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image Banner'),
        ),
        migrations.AddField(
            model_name='event',
            name='image_flyer',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image Flyer'),
        ),
    ]
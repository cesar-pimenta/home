# Generated by Django 4.1.7 on 2023-03-03 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apelido',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

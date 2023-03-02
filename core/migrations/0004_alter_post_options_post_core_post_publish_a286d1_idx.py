# Generated by Django 4.1.7 on 2023-03-01 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish']},
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-publish'], name='core_post_publish_a286d1_idx'),
        ),
    ]

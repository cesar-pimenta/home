# Generated by Django 4.1.7 on 2023-03-08 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvenType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Tipo de Evento',
                'verbose_name_plural': 'Tipos de Evento',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('date_ini', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.eventype')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]

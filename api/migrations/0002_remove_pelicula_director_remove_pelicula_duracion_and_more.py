# Generated by Django 4.0.3 on 2022-03-09 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='director',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='duracion',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='titulo',
        ),
    ]

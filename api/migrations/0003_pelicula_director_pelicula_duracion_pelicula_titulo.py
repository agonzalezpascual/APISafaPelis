# Generated by Django 4.0.3 on 2022-03-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_pelicula_director_remove_pelicula_duracion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='director',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pelicula',
            name='duracion',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pelicula',
            name='titulo',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]

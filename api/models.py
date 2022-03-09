from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    duracion = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


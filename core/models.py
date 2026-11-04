from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    sexo = models.CharField(max_length=20)
    edadAproximada = models.PositiveBigIntegerField()
    imagen = models.URLField()

    especie = models.ForeignKey(Especie, on_delete=models.PROTECT, related_name="mascotas")

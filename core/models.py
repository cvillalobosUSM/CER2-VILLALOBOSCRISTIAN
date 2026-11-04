from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    sexo = models.CharField(max_length=20)
    edadAproximada = models.PositiveBigIntegerField()
    imagen = models.URLField()

    especie = models.ForeignKey(Especie, on_delete=models.PROTECT, related_name="mascotas")

    def __str__(self):
        return str(self.nombre)

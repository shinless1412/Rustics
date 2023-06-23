from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=250)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

# Create your models here.

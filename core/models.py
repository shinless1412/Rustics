from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=250, verbose_name="Descripcion")
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', verbose_name="imagen", null=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'   

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    contenido = models.TextField()
    puntuacion = models.IntegerField()

    def __str__(self):
        return self.contenido




# Create your models here.
# xd
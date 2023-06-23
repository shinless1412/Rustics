from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=250, verbose_name="Descripcion")
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', verbose_name="imagen", null=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'   

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()



# Create your models here.
# xd
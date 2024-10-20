from django.db import models
from apps.restaurante.models import Restaurante

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=9, decimal_places=3)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre


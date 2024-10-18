from django.db import models
from apps.orden.models import Pedido

# Create your models here.
class Fcatura(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.SET_NULL)
    total = models.DecimalField(max_digits=9, decimal_places=3)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Factura del pedido {self.pedido.id}"

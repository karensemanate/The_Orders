from django.db import models
from apps.orden.models import Pedido

class PedidoCocina(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=Pedido.ESTADO, default='E')

    def __str__(self):
        return f"El pedido en la cocina de {self.pedido.id}"

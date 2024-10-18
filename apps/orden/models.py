from django.db import models
from apps.producto.models import Producto
from apps.mesa.models import Mesa

class Pedido(models.Model):
    nombre_del_cliente = models.CharField(max_length=50)
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True)
    para_llevar = models.BooleanField(default=False)
    tiempo_creado = models.DateTimeField(auto_now_add=True)

    ESTADO = [
        ('E', 'En espera'),
        ('P', 'Preparado'),
        ('L', 'Listo'),
        ('S', 'Servido'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO, default='E')

    def __str__(self):
        return f"El pedido {self.id} del cliente {self.nombre_del_cliente}"

class nPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, related_name='items', null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveBigIntegerField()
    observaciones = models.TextField()

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"


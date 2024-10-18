from rest_framework import viewsets
from apps.orden.models import Pedido, nPedido
from .serializer import OrderItemSerializer, PedidoSerializer

class PedidoView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemPedidoView(viewsets.ModelViewSet):
    queryset = nPedido.objects.all()
    serializer_class = OrderItemSerializer
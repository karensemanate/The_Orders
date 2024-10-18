from rest_framework import viewsets
from apps.orden.models import Pedido, nPedido
from .serializers import OrderItemSerializer, OrdenSerializer

class PedidoView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = OrdenSerializer

class ItemPedidoView(viewsets.ModelViewSet):
    queryset = nPedido.objects.all()
    serializer_class = OrderItemSerializer
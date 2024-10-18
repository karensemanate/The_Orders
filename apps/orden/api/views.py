from rest_framework import viewsets
from apps.orden.models import Pedido, nPedido
from .serializers import OrderSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = OrderSerializer
    
from rest_framework import viewsets
from apps.producto.models import Producto
from apps.producto.api.serializer import ProductoSerializer

class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

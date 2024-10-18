from rest_framework import viewsets
from apps.restaurante.models import Restaurante
from apps.restaurante.api.serializer import RestaurantSerializer

class RestauranteView(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestaurantSerializer

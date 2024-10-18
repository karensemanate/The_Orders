from rest_framework import viewsets
from apps.restaurante.models import Restaurante
from apps.restaurante.api.serializers import RestauranteSerializer

class RestauranteView(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

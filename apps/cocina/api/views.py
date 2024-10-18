from rest_framework import viewsets
from apps.cocina.models import PedidoCocina
from apps.cocina.api.serializers import CocinaSerializer

class PedidoCocinaView(viewsets.ModelViewSet):
    queryset = PedidoCocina.objects.all()
    serializer_class = CocinaSerializer

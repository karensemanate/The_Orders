from rest_framework import viewsets
from apps.mesa.models import Mesa
from apps.mesa.api.serializers import MesaSerializer

class TableView(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
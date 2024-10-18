from rest_framework import viewsets
from apps.factura.models import Factura
from apps.factura.api.serializer import FacturaSerializer

class FacturaView(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

from rest_framework import viewsets
from apps.factura.models import Fcatura
from apps.factura.api.serializers import FacturaSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Fcatura.objects.all()
    serializer_class = FacturaSerializer
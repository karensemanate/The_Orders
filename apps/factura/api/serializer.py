from rest_framework import serializers
from apps.factura.models import Fcatura

class FcaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fcatura
        fields = '_all_'
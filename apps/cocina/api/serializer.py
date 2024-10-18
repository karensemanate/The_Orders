from rest_framework import serializers
from apps.cocina.models import PedidoCocina

class cocinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCocina
        fields = '_all_'
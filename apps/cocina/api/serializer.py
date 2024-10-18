from rest_framework import serializers
from apps.cocina.models import PedidoCocina

class CocinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCocina
        fields = '__all__'

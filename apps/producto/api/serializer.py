from rest_framework import serializers
from apps.producto.models import Producto

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '_all_'
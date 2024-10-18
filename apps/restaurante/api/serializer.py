from rest_framework import serializers
from apps.restaurante.models import Restaurante

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '_all_'
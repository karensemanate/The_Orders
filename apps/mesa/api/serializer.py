from rest_framework import serializers
from apps.mesa.models import Mesa

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '_all_'
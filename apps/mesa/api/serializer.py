from rest_framework import serializers
from apps.mesa.models import Mesa

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '_all_'
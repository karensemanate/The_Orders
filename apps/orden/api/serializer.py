from rest_framework import serializers
from apps.orden.models import Pedido, nPedido

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = nPedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Pedido.objects.create(**validated_data)
        for item_data in items_data:
            nPedido.objects.create(order=order, **item_data)
        return order

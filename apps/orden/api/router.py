from rest_framework.routers import DefaultRouter
from apps.orden.api.views import PedidoView, ItemPedidoView

router = DefaultRouter()
router.register(r'pedidos', PedidoView, basename='pedido')
router.register(r'item-pedidos', ItemPedidoView, basename='item-pedido')

urlpatterns = router.urls

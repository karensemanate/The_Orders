from rest_framework.routers import DefaultRouter
from apps.cocina.api.views import PedidoCocinaView

router = DefaultRouter()
router.register(r'pedidos-cocina', PedidoCocinaView, basename='pedido-cocina')

urlpatterns = router.urls

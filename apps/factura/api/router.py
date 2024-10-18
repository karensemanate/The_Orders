from rest_framework.routers import DefaultRouter
from apps.factura.api.views import FacturaView

router = DefaultRouter()
router.register(r'facturas', FacturaView, basename='factura')

urlpatterns = router.urls

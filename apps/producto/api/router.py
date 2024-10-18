from rest_framework.routers import DefaultRouter
from apps.producto.api.views import ProductView

router = DefaultRouter()
router.register(r'productos', ProductView, basename='producto')

urlpatterns = router.urls

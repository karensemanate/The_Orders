from rest_framework.routers import DefaultRouter
from apps.producto.api.views import ProductoView

router = DefaultRouter()
router.register(r'productos', ProductoView, basename='producto')

urlpatterns = router.urls

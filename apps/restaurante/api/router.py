from rest_framework.routers import DefaultRouter
from apps.restaurante.api.views import RestauranteView

router = DefaultRouter()
router.register(r'restaurantes', RestauranteView, basename='restaurante')

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from apps.mesa.api.views import MesaView

router = DefaultRouter()
router.register(r'mesas', MesaView, basename='mesa')

urlpatterns = router.urls

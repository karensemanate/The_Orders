"""
URL configuration for The_Order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.restaurante.api.router import router as ResRouter
from apps.producto.api.router import router as ProRouter
from apps.mesa.api.router import router as MesRouter
from apps.orden.api.router import router as OrdRouter
from apps.factura.api.router import router as FacRouter
from apps.cocina.api.router import router as CocRouter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/restaurantes/', include(ResRouter.urls)),
    path('api/productos/', include(ProRouter.urls)),
    path('api/mesas/', include(MesRouter.urls)),
    path('api/pedidos/', include(OrdRouter.urls)),
    path('api/facturas/', include(FacRouter.urls)),
    path('api/cocina/', include(CocRouter.urls)),
]

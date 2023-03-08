from django.contrib import admin
from django.urls import path,include, re_path
from rest_framework import routers
from clientes.views import ClientesViewSet
from django.urls import re_path as url

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

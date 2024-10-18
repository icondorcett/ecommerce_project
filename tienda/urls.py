# tienda/urls.py
from django.urls import path
from .views import ProductoList, CompraList

urlpatterns = [
    path('api/productos/', ProductoList.as_view(), name='producto-list'),
    path('api/compras/', CompraList.as_view(), name='compra-list'),
]

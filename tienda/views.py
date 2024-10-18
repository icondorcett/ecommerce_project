from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Producto, Compra
from .serializers import ProductoSerializer, CompraSerializer
from rest_framework.permissions import IsAuthenticated

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CompraList(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(cliente=self.request.user)

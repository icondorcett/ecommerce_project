from django.db import models

# Create your models here.

from django.contrib.auth.models import User  # Para la relación con el cliente
from django.utils import timezone

class Producto(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre del producto")
    description = models.TextField(verbose_name="Descripción del producto", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(verbose_name="Cantidad disponible")

    def __str__(self):
        return self.name

class Compra(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cliente")
    productos = models.ManyToManyField(Producto, related_name="compras", verbose_name="Productos")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    fecha = models.DateTimeField(default=timezone.now, verbose_name="Fecha de la compra")

    def __str__(self):
        return f"Compra #{self.id} - {self.cliente.username}"



class Carrito(models.Model):
    cliente = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Cliente")
    productos = models.ManyToManyField('Producto', through='CarritoItem', related_name='en_carrito', verbose_name="Productos")

    def __str__(self):
        return f"Carrito de {self.cliente.username}"

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.name}"

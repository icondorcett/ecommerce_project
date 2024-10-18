from django.contrib import admin

# Register your models here.

from .models import Carrito, Compra, Producto, CarritoItem
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Definir el Inline para CarritoItem
class CarritoItemInline(admin.TabularInline):  # O usar StackedInline si prefieres ese estilo
    model = CarritoItem
    extra = 1  # Número de formularios adicionales vacíos para agregar nuevos items

def finalizar_compra(modeladmin, request, queryset):
    for carrito in queryset:
        total = 0
        productos_seleccionados = []
        
        # Crear una compra
        compra = Compra.objects.create(
            cliente=carrito.cliente,
            total=0,  # Se calculará luego
            fecha=timezone.now()
        )

        # Agregar los productos del carrito a la compra
        for item in carrito.carritoitem_set.all():
            if item.producto.stock >= item.cantidad:
                productos_seleccionados.append(item.producto)
                total += item.producto.price * item.cantidad

                # Reducir el stock del producto
                item.producto.stock -= item.cantidad
                item.producto.save()

            else:
                # Podrías lanzar una excepción o alertar al administrador si no hay stock suficiente
                print(f"No hay suficiente stock de {item.producto.name}")
        
        compra.productos.set(productos_seleccionados)
        compra.total = total
        compra.save()

        # Limpiar el carrito del cliente
        carrito.productos.clear()

finalizar_compra.short_description = "Finalizar la compra y reducir stock"

# Clase personalizada para el Admin de Clientes
class ClienteAdminSite(admin.AdminSite):
    site_header = 'Panel de Cliente'
    site_title = 'Administración de Cliente'
    index_title = 'Bienvenido al Panel de Cliente'

    def has_permission(self, request):
        # Permite el acceso solo si el usuario es un cliente
        return request.user.is_active and request.user.groups.filter(name='clientes').exists()

# Crea una instancia del nuevo AdminSite
cliente_admin_site = ClienteAdminSite(name='cliente_admin')



@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id','cliente', 'cliente__first_name','cliente__last_name','cliente__email')
    list_display_links = ('cliente',)
    actions = [finalizar_compra]
    inlines = [CarritoItemInline]  # Agregar el inline aquí

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','name','description', 'price', 'stock')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('price',)
    ordering = ('name',)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','cliente__first_name','cliente__last_name','cliente__email', 'total', 'fecha')
    list_display_links = ('cliente',)
    search_fields = ('cliente__username', 'total')
    list_filter = ('fecha',)
    ordering = ('fecha',)


@admin.register(Compra, site=cliente_admin_site)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','cliente__first_name','cliente__last_name','cliente__email', 'total', 'fecha')
    list_display_links = ('cliente',)
    search_fields = ('cliente__username', 'total')
    list_filter = ('fecha',)
    ordering = ('fecha',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filtrar para que solo muestre las compras del usuario autenticado si es un cliente
        if request.user.groups.filter(name='clientes').exists():
            return qs.filter(cliente=request.user)
        return qs

@admin.register(Carrito,site=cliente_admin_site)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id','cliente', 'cliente__first_name','cliente__last_name','cliente__email')
    list_display_links = ('cliente',)
    actions = [finalizar_compra]
    inlines = [CarritoItemInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filtrar para que solo muestre los carritos del usuario autenticado si es un cliente
        if request.user.groups.filter(name='clientes').exists():
            return qs.filter(cliente=request.user)
        return qs
    
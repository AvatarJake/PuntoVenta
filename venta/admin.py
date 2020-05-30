from django.contrib import admin
from .models import *
from venta.models import Venta, VentaDetalle
from producto.models import Producto
from django.db.models import Sum


class VentaDetalleInline(admin.TabularInline):
	model=VentaDetalle
	extra=0		

class VentaAdmin(admin.ModelAdmin):
	"""docstring for Comprobante"""
	inlines=[VentaDetalleInline]
	search_fields=['producto_nombre','producto_codigo', 'producto_descripcion']
	list_filter=['fechaVenta']
	list_display = ['cliente', 'fechaVenta','noFactura', 'total']

admin.site.register(Venta, VentaAdmin)
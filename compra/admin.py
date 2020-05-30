from django.contrib import admin
from .models import *
from django.db.models import Sum
 

class CompraDetalleInline(admin.TabularInline):
	model=CompraDetalle
	extra=0		

class CompraAdmin(admin.ModelAdmin):
	"""docstring for Comprobante"""
	inlines=[CompraDetalleInline]
	search_fields=['producto_nombre','producto_codigo', 'producto_descripcion']
	list_filter=['fechaCompra']
	list_display = ['proveedor', 'fechaCompra','noFactura','fechaFactura','total','observacion']


		

admin.site.register(Compra, CompraAdmin)
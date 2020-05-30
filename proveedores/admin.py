from django.contrib import admin
from .models import *


class ProveedorAdmin(admin.ModelAdmin):
	actions = ['inactivar', 'activar']
	search_fields = ['nombre', 'nit']
	list_display = ['nit','nombre','telefono','direccion', 'correo', 'activo']

	#Opciones para activar y desactivar Clientes

	def inactivar(self, request, queryset):

		for row in queryset.filter(activo=True):
			self.log_change(request, row, 'inactivar proveedor')
		rows_updated = 0

		for obj in queryset:
			if obj.activo:
				obj.activo = False
				obj.save()

				rows_updated += 1

		if rows_updated == 1:
			message_bit = "1 proveedor se marco"
		else:
			message_bit = "%s proveedores se marcaron" % rows_updated
		self.message_user(
			request, "%s satisfactoriamente como inactivas" % message_bit)
	inactivar.short_description = 'Inactivar proveedor'


	def activar(self, request, queryset):

		for row in queryset.filter(activo=False):
			self.log_change(request, row, 'activar proveedor')
		rows_updated = 0

		for obj in queryset:
			if not obj.activo:
				obj.activo = True
				obj.save()

				rows_updated += 1

		if rows_updated == 1:
			message_bit = "1 proveedor se marco"
		else:
			message_bit = "%s proveedores se marcaron" % rows_updated
		self.message_user(
			request, "%s satisfactoriamente como activos" % message_bit)
	activar.short_description = 'Activar proveedor'

admin.site.register(Proveedor, ProveedorAdmin)
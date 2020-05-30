from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
	actions = ['inactivar', 'activar']
	search_fields = ['nombre', 'apellido', 'nit']
	list_filter = ['genero']
	list_display = ['nit','nombre', 'apellido','genero','telefono','activo']

	#Opciones para activar y desactivar Clientes

	def inactivar(self, request, queryset):

		for row in queryset.filter(activo=True):
			self.log_change(request, row, 'inactivar cliente')
		rows_updated = 0

		for obj in queryset:
			if obj.activo:
				obj.activo = False
				obj.save()

				rows_updated += 1

		if rows_updated == 1:
			message_bit = "1 cliente se marco"
		else:
			message_bit = "%s clientes se marcaron" % rows_updated
		self.message_user(
			request, "%s satisfactoriamente como inactivas" % message_bit)
	inactivar.short_description = 'Inactivar cliente'


	def activar(self, request, queryset):

		for row in queryset.filter(activo=False):
			self.log_change(request, row, 'activar cliente')
		rows_updated = 0

		for obj in queryset:
			if not obj.activo:
				obj.activo = True
				obj.save()

				rows_updated += 1

		if rows_updated == 1:
			message_bit = "1 cliente se marco"
		else:
			message_bit = "%s clientes se marcaron" % rows_updated
		self.message_user(
			request, "%s satisfactoriamente como activos" % message_bit)
	activar.short_description = 'Activar cliente'

admin.site.register(Cliente, ClienteAdmin)
# Register your models here.

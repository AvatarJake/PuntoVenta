from django.contrib import admin
from .models import *
from django.template.loader import get_template
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin
from django.utils import timezone
from .models import Producto

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class ProductoAdmin(ImportExportModelAdmin,ExportMixin,admin.ModelAdmin):
    actions = ['inactivar', 'activar', 'imprimir']

    search_fields = ['codigo', 'nombre']
    list_filter = ['nombre']
    list_display = ['codigo', 'nombre', 'marca', 'descripcion','existencias', 'precioCompra', 'precioVenta', 'activo']
    resource_class = ProductoResource

    #acciones para imprimir productos


#activar y desactivar productos
   
    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar producto')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 producto se marco"
        else:
            message_bit = "%s productos se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar prodcuto'



    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar producto')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 producto se marco"
        else:
            message_bit = "%s productos se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar producto'

admin.site.register(Producto, ProductoAdmin)
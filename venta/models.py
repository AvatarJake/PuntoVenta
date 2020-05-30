from django.db import models
#from bases.models import ClaseModelo
from producto.models import Producto
from cliente.models import Cliente



class Venta(models.Model):
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	fechaVenta = models.DateField('Fecha de Compra', null=True, blank=True)
	noFactura = models.CharField(max_length=100,null=True)
	total = models.FloatField(default=0.00)

	
	def __str__(self):
		return'{}'.format(self.noFactura)

			
		class Meta:
			db_table = 'venta'
			verbose_name = 'Venta'
			verbose_name_plural = 'Ventas'

class VentaDetalle(models.Model):
	venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
	cantidad = models.PositiveIntegerField('cantidad',default=0)
	precio = models.FloatField('precio', default=0)
	subtotal =  models.FloatField('subtotal', default=0)
	
	
	def __str__(self):
		return '{}'.format(self.producto)

	def save(self, *args, **kwargs):
		
		self.precio = self.producto.precioVenta
		self.subtotal = float(float(int(self.cantidad)) * self.precio)

		if self.venta.total==0.00:
			self.venta.total=float(self.subtotal)
		else:
			self.venta.total+= self.subtotal
		
		self.producto.existencias -= self.cantidad	
		
		self.venta.save()
		self.producto.save()
		super(VentaDetalle,self).save()


	
		class Meta:
			db_table = 'venta_detalle'
			verbose_name = 'Detalle Venta'
			verbose_name_plural = 'Detalles Ventas'

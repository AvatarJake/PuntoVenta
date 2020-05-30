from django.db import models
#from bases.models import ClaseModelo
from producto.models import Producto
from proveedores.models import Proveedor




class Compra(models.Model):
	proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE, null=True, blank=True)
	fechaCompra = models.DateField('Fecha de Compra', null=True, blank=True)
	observacion = models.TextField(blank=True, null=True)
	noFactura = models.CharField(max_length=100,null=True)
	fechaFactura = models.DateField('Fecha Factura',null=True, blank=True)
	total = models.FloatField(default=0.00)

	
	def __str__(self):
		return'{}'.format(self.proveedor, self.observacion)

	def save(self, *args, **kwargs):
		
		self.observacion=self.observacion.upper()
			

		super(Compra,self).save()
		
		class Meta:
			db_table = 'compra'
			verbose_name = 'Compra'
			verbose_name_plural = 'Compras'

class CompraDetalle(models.Model):
	
	compra = models.ForeignKey(Compra,on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
	cantidad = models.PositiveIntegerField('cantidad',default=0)
	precioCompra =  models.FloatField('precioCompra',default=0)
	precioVenta = models.FloatField('precioVenta',default=0)
	subtotal =  models.FloatField('subtotal',default=0)
	utilidad = models.FloatField('utilidad',default=0)
	
	def __str__(self):
		return '{}'.format(self.producto)

	def save(self, *args, **kwargs):
		
		if self.subtotal==0.00:
			self.subtotal = float(float(int(self.cantidad)) * self.precioCompra)

		self.utilidad= float(float(int(self.cantidad)) * self.precioVenta) - self.subtotal

		if self.compra.total==0.00:
			self.compra.total=float(self.subtotal)
		else:
			self.compra.total+= self.subtotal
		
		if self.producto.existencias==0:
			self.producto.existencias = self.cantidad
		else:
			self.producto.existencias += self.cantidad	

		self.producto.precioCompra = self.precioCompra
		self.producto.precioVenta = self.precioVenta
		
		self.compra.save()
		self.producto.save()
		super(CompraDetalle,self).save()



	#@property
	#def resultado(self):
	#	return (self.precioVenta - self.precioCompra)
		
	#def b (self):
	#	valor2 = self.resultado * self.cantidad
	#	super (CompraDetalle, self).b()


	#def __unicode__(self):
	#	return "%s %s" % (self.producto, self.cantidad, self.precioCompra, self.precioVenta, self.ganancia)
	
		class Meta:
			db_table = 'compra_detalle'
			verbose_name = 'Detalle Compra'
			verbose_name_plural = 'Detalles Compras'

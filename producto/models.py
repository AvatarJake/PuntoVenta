from django.db import models
from django.utils.safestring import mark_safe
	

class Producto(models.Model):
	def number():
		num = Producto.objects.count()
		if num == None:
			return 1
		else:
			return num + 1


	codigo = models.IntegerField('codigo', unique=True, default=number, editable=False)
	nombre = models.CharField('nombre', max_length=50)
	marca = models.CharField('marca', max_length=50,null=True)
	descripcion = models.CharField('descripcion', max_length=100)
	existencias = models.IntegerField('existencias', default=0,null=True)
	precioCompra =  models.FloatField(default=0)
	precioVenta = models.FloatField(default=0)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s %s' % (self.nombre, self.marca)
	
	def clean(self): # BEFORE INSERT OR UPDATE
		super(Producto, self).clean()

	
	def save(self, **kwargs): # AFTER INSERT OR UPDATE

		if self.activo:
			self.nombre = self.nombre.upper()
			self.marca = self.marca.upper()
			self.descripcion = self.descripcion.upper()
		else:
			self.nombre = self.nombre.lower()
			self.marca = self.marca.lower()
			self.descripcion = self.descripcion.lower()
		super(Producto, self).save()

	class Meta():
		db_table = 'producto'
		verbose_name= 'Producto'
		verbose_name_plural= 'Productos'
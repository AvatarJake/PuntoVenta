
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


GENERO_OPCIONES=(
	('M', 'Masculino'),
	('F', 'Femenino'),
	)

class Proveedor(models.Model):
	nit = models.CharField('NIT', max_length=10, unique=True)
	nombre = models.CharField('nombre', max_length=50, null=True)
	telefono = PhoneNumberField()
	direccion = models.CharField('direccion', max_length=100)
	correo = models.EmailField('email', null=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s %s' % (self.nombre, self.direccion)

	def clean(self): # BEFORE INSERT OR UPDATE
		super(Proveedor, self).clean()


	def save(self, **kwargs): # AFTER INSERT OR UPDATE

		if self.activo:
			self.nombre.upper()
			
		else:
			self.nombre = self.nombre.lower()
			
		super(Proveedor, self).save()

	class Meta():
		db_table = 'proveedor'
		verbose_name= 'Proveedor'
		verbose_name_plural= 'Proveedores'
	
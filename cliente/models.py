
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


GENERO_OPCIONES=(
	('M', 'Masculino'),
	('F', 'Femenino'),
	)

class Cliente(models.Model):
	nit = models.CharField('NIT', max_length=10, unique=True)
	nombre = models.CharField('nombre', max_length=50)
	apellido = models.CharField('apellido', max_length=50)
	genero= models.CharField('genero', max_length=1, choices=GENERO_OPCIONES, default='M')
	telefono = PhoneNumberField()
	direccion = models.CharField('direccion', max_length=100)
	correo = models.EmailField('email')
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)

	def clean(self): # BEFORE INSERT OR UPDATE
		super(Cliente, self).clean()


	def save(self, **kwargs): # AFTER INSERT OR UPDATE

		if self.activo:
			self.nombre = self.nombre.upper()
			self.apellido = self.apellido.upper()
		else:
			self.nombre = self.nombre.lower()
			self.apellido = self.apellido.lower()

		super(Cliente, self).save()

	class Meta():
		db_table = 'cliente'
		verbose_name= 'Cliente'
		verbose_name_plural= 'Clientes'
		unique_together = ['nombre','apellido']
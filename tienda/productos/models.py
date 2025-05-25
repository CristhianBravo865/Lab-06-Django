from django.db import models

class Producto(models.Model):
	codigo = models.CharField(max_length=100, unique=True)
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	precio = models.DecimalField(max_digits=10, decimal_places=2)
 
	def __str__(self):
		return self.nombre
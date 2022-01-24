from django.db import models

# Create your models here.
class Bancos(models.Model):
    nombre=models.CharField(max_length=60)
    numero_banco=models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):
    nombre=models.CharField(max_length=60)
    nombre_producto=models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'

class Tasa(models.Model):
    nombre=models.CharField(max_length=60)
    tipo_tasa=models.IntegerField()

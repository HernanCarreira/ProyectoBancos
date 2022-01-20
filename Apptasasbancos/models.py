from django.db import models

# Create your models here.
class Bancos(models.Model):
    nombre=models.CharField(max_length=60)
    numero_banco=models.IntegerField()

class Producto(models.Model):
    nombre=models.CharField(max_length=60)
    nombre_producto=models.IntegerField()

class Tasa(models.Model):
    nombre=models.CharField(max_length=60)
    tipo_tasa=models.IntegerField()

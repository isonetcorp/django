from django.db import models
from django.shortcuts import render
from .validators import validar_minimo_caracteres 
from .validators import validar_maximo_caracteres 
from .validators import validar_no_campo_vacio 
from .validators import validar_campo_string 



class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_minimo_caracteres,validar_maximo_caracteres]) 

    def __str__(self):
        return self.nombre
    
class TipoGasto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    nombre_tipo_gasto = models.CharField(max_length=100,validators=[validar_no_campo_vacio,validar_minimo_caracteres])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "TipoGasto - %s" % self.nombre_tipo_gasto    

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100,validators=[validar_no_campo_vacio,validar_minimo_caracteres])
    direccion = models.CharField(max_length=100,validators=[validar_minimo_caracteres,validar_maximo_caracteres])
    def __str__(self):
        return "Proveedor - %s" % self.nombre_proveedor    


class Gasto(models.Model):
    tipo_gasto = models.ForeignKey(TipoGasto, on_delete=models.CASCADE) 
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE) 
    fecha_hora = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=200,validators=[validar_minimo_caracteres,validar_maximo_caracteres,validar_campo_string])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Gasto - %s" % self.description


class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'
    PAQUETE = "Pq", 'Paquete'
    METRO= "Mtr", 'Metros'
    CAJA= "Cja", 'Caja'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    unidades = models.CharField(max_length=3, choices=ProductUnits.choices, default=ProductUnits.UNITS)
    disponible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
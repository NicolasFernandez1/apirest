from django.db import models

# Create your models here.

class Cliente(models.Model): 
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=10  )
    email = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50,)


    

    def __str__(self):
        return self.nombre




class Producto(models.Model):   
    ids = models.CharField(max_length=1000, primary_key=True)
    nombre = models.CharField(max_length=10)
    asunto = models.CharField(max_length=50)
    precio = models.CharField(max_length=20 )
    
    

    def __str__(self):
        return self.nombre



class Comprar(models.Model):
    Producto = models.CharField(max_length=100, verbose_name='Producto')
    Cantidad = models.CharField(max_length=100, verbose_name='Cantidad')
    Tipotarjeta = models.CharField(max_length=100, verbose_name='Tipotarjeta')
    Numerotarjeta=models.CharField(max_length=100,primary_key=True,verbose_name='Numerotarjeta')
    Fecha_expira=models.CharField(max_length=100, verbose_name='Fecha_expira')
    Cvv=models.CharField(max_length=100,verbose_name='CVV')
    Direccion=models.CharField(max_length=100,verbose_name='Direccion')

    def int(self):
        return self.Numerotarjeta
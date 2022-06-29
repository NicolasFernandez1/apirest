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
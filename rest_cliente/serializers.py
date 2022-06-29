from rest_framework import serializers
from core.models import Cliente, Producto



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:

  
        model = Cliente
        fields =['rut', 'nombre','email','direccion']
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Producto
        fields =['ids','nombre', 'asunto', 'precio']
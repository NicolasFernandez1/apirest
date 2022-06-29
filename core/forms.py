from django import forms
from django.forms import ModelForm
from .models import *


class ClienteForm(ModelForm):
    class Meta:
        widgets={
            'rut': forms.TextInput(    
                attrs={
                    'placeholder': 'ingrese rut',    
                    'name': 'rut'}
            ),
            'nombre': forms.TextInput(    
                attrs={
                    'placeholder': 'ingrese nombre del producto ',    
                    'name': 'nombre'
                }
            ),
            'email': forms.TextInput(    
                attrs={
                    'placeholder': 'ingrese email',
                    'name': 'email'}
            ),
            'direccion': forms.TextInput(    
                attrs={
                    'placeholder': 'ingrese direccion', 
                    'name': 'direccion'}
            )

        }
  
        model = Cliente
        fields =['rut', 'nombre','email','direccion']
        
class ProductoForm(ModelForm):
    class Meta:
        widgets={
            'ids': forms.NumberInput(    
                attrs={
                    'placeholder': 'ingrese el id del producto',    
                    'name': 'ids'}
                
            ),
            'nombre': forms.TextInput(    
                attrs={
                    'placeholder': 'ingrese nombre del producto ',    
                    'name': 'nombre'}
                
            ),
            'asunto': forms.TextInput(    
                attrs={
                    'placeholder': 'ingrese asunto',
                    'name': 'asunto'} 
            ),
            'precio': forms.TextInput(    
                attrs={
                    'placeholder': 'ingrese precio', 
                    'name': 'precio'} 
            )

         }
        model = Producto
        fields =['ids','nombre', 'asunto', 'precio']


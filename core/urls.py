from os import name
from django import views
from django.urls import path



from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('home.html',home,name="home"),
    path('home2.html',home2,name="home2"),
    path('home3.html',home3,name="home3"),
    path('contacto.html',contacto,name="contacto"),
    path('login.html',login,name="login"),
    path('Registro.html',Registro,name="Registro"),
    path('BandanaB.html',BandanaB,name="BandanaB"),
    path('BandanaF.html',BandanaF,name="BandanaF"),
    path('ArnesN.html',ArnesN,name="ArnesN"),
    path('ArnesF.html',ArnesF,name="ArnesF"),
    path('CollarP.html',CollarP,name="CollarP"),
    path('CollarH.html',CollarH,name="CollarH"),
    path('HuesoP.html',HuesoP,name="HuesoP"),
    path('HuesoP.html',HuesoPJ,name="HuesoPJ"),
    path('productos.html',productos,name="productos"),
    path('mostrarP.html',mostrarP,name="mostrarP"),
    path('mostrarC.html',mostrarC,name="mostrarC"),
    path('clientes.html',clientes,name="clientes"),
    path('crearP.html',crearP,name="crearP"),
    path('modificarP.html/<id>',modificarP,name="modificarP"),
    path('eliminarP.html/<id>',eliminarP,name="eliminarP"),
    path('crearC.html',crearC,name="crearC"),
    path('modificarC.html/<id>',modificarC,name="modificarC"),
    path('eliminarC.html/<id>',eliminarC,name="eliminarC"),


    
]
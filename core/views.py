import email
from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render 
from .models import *
from .forms import *




# Create your views here.

def home(request):

    return render(request, 'core/home.html')
    

def home2(request):

    return render(request, 'core/home2.html')

def home3(request):

    return render(request, 'core/home3.html')

def contacto(request):

    return render(request, 'core/contacto.html')

def login(request):

    return render(request, 'core/login.html')

def Registro(request):
   

    return render(request, 'core/Registro.html')

def BandanaB(request):

    return render(request, 'core/BandanaB.html')

def BandanaF(request):

    return render(request, 'core/BandanaF.html')

def ArnesN(request):

    return render(request, 'core/ArnesN.html')

def ArnesF(request):

    return render(request, 'core/ArnesF.html')

def CollarP(request):

    return render(request, 'core/CollarP.html')

def CollarH(request):

    return render(request, 'core/CollarH.html')


def HuesoP(request):

    return render(request, 'core/HuesoP.html')

def HuesoPJ(request):

    return render(request, 'core/HuesoPJ.html')

def productos(request):

    return render(request, 'core/productos.html')

def mostrarP(request):
    panimal=Producto.objects.all()
    return render(request, 'core/mostrarP.html', {"panimal":panimal})

def mostrarC(request):
    clientess=Cliente.objects.all()
    return render(request, 'core/mostrarC.html', {"clientess":clientess})

def clientes(request):
    
    return render(request, 'core/clientes.html')

def crearC(request):

    return render(request, 'core/crearC.html')

def crearP(request):

    if request.method=="POST":
        form=ProductoForm(request.POST)
        form.save()
        return redirect( 'mostrarP.html')
        
    return render(request, 'core/crearP.html', {"crearformP":ProductoForm()})


def modificarP(request, id):
    
    prod=Producto.objects.get(ids=id)
    if request.method=="POST":
        form=ProductoForm(request.POST, instance=prod)
        form.save()
        return redirect('mostrarP')
    return render(request, 'core/modificarP.html', {"modificarformP":ProductoForm(instance=prod)})

def eliminarP(request, id):
    prod=Producto.objects.get(ids=id)
    prod.delete()
    return redirect('mostrarP')

def crearC(request):

    if request.method=="POST":
        form=ClienteForm(request.POST)
        form.save()
        return redirect( 'mostrarC.html')
    else:
        form=ClienteForm()
    return render(request, 'core/crearC.html', {"crearformC":form})

def modificarC(request, id):
    
    prod=Cliente.objects.get(rut=id)
    if request.method=="POST":
        form=ClienteForm(request.POST, instance=prod)
        form.save()
        return redirect('mostrarC')
    return render(request, 'core/modificarC.html', {"modificarformC":ClienteForm(instance=prod)})

def eliminarC(request, id):
    prod=Cliente.objects.get(rut=id)
    prod.delete()
    return redirect('mostrarC')

def Compra(request):



    return render(request, 'core/Compra.html')

def registrar_compra(request):
    datos={

    }
    Producto=request.POST['Producto']
    Cantidad=request.POST['Cantidad']
    Tipotarjeta=request.POST['Tipotarjeta']
    Numerotarjeta=request.POST['Numerotarjeta']
    Fecha_expira=request.POST['Fecha_expira']
    Cvv=request.POST['Cvv']
    Direccion=request.POST['Direccion']

    datos['mensaje']= "Registro completado"
    codigo=Comprar.objects.create(Producto=Producto,Cantidad=Cantidad,Tipotarjeta=Tipotarjeta,Numerotarjeta=Numerotarjeta,Fecha_expira=Fecha_expira,Cvv=Cvv,Direccion=Direccion)
    return render(request, 'core/Compra_completo.html')

def consultarcompra_datos(request):

    return render (request, 'core/consultarcompra-datos.html')

def consultarcompra_registro(request):
    datos={

    }
    Numerotarjeta=request.POST['Numerotarjeta']
    codigo=Comprar.objects.filter(Numerotarjeta=Numerotarjeta)

    if codigo:
        datos['mensaje']= "Usuario encontrado correctamente"
        Comprarx=Comprar.objects.get(Numerotarjeta=Numerotarjeta)
        datos['Comprar']=Comprarx
        return render (request, 'core/consultarcompra-registro.html',datos)
    else:
        datos['mensaje'] = "Usuario no encontrado"
        return render (request, 'core/consultarcompra-registro.html',datos)

def form_mod_Compra(request,id):
    persona= Comprar.objects.get(Numerotarjeta=id)

    datos= {
        'form': ComprarForm(instance=persona),
        'Persona':persona

    }
    return render(request, 'core/form_mod_compra.html',datos)
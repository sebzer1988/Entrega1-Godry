from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Context, Template, loader
from Mascotas.forms import *

def inicio(request):
    return render (request, "Mascotas/inicio.html")

def perros(request):
    if request.method=="POST":
        form=PerroForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            raza=informacion["raza"]
            edad=informacion["edad"]
            perro=Perro(nombre=nombre, raza=raza, edad=edad)
            perro.save()
            return render(request, "Mascotas/inicio.html", {"mensaje":"Perro creado"})
    else:
        formulario=PerroForm()
        return render (request, "Mascotas/perros.html", {"formulario":formulario})

def gatos(request):
    if request.method=="POST":
        form=GatoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            raza=informacion["raza"]
            edad=informacion["edad"]
            gato=Gato(nombre=nombre, raza=raza, edad=edad)
            gato.save()
            return render(request, "Mascotas/inicio.html", {"mensaje":"Gato creado"})
    else:
        formulario=GatoForm()
        return render (request, "Mascotas/gatos.html", {"formulario":formulario})

def animales(request):
    if request.method=="POST":
        form=AnimalForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            animal_tipo=informacion["animal_tipo"]
            edad=informacion["edad"]
            animal=Animal(nombre=nombre, animal_tipo=animal_tipo, edad=edad)
            animal.save()
            return render(request, "Mascotas/inicio.html")
    else:
        formulario=AnimalForm()
        return render (request, "Mascotas/animales.html", {"formulario":formulario})

def busquedaPerro(request):
    return render(request, "Mascotas/busquedaPerro.html")

def buscar(request):
    if request.GET["raza"]:
        raza=request.GET["raza"]
        #Ahi se va a buscar dentro de todos los perros, los que tienen la raza buscada
        perros=Perro.objects.filter(raza=raza)
        return render(request, "Mascotas/resultadosBusqueda.html", {"perros":perros})
    else:
        return render(request, "Mascotas/busquedaPerro.html", {"mensaje":"Ingrese una raza de perro"} )
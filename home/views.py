from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.forms import FormMascota, BusquedaMascota
from home.models import Mascota

def index (request):

    return render(request, 'index.html')

def alta_mascota(request):
    if request.method == 'POST':
        print(request.POST)
        formulario = FormMascota(request.POST)
        
        if formulario.is_valid():
            data=formulario.cleaned_data

            nombre=data['nombre']
            duenio=data['duenio']
            edad=data['edad']
                        
            mascota = Mascota(nombre=nombre, duenio=duenio, edad=edad)
            mascota.save()
            
            return redirect('ver_mascotas')
    formulario = FormMascota()
    
    return render(request, 'alta_mascota.html', {'formulario': formulario})

def ver_mascotas(request):
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        mascotas = Mascota.objects.filter(nombre__icontains=nombre)
    else:
        mascotas = Mascota.objects.all()
        
    formulario = BusquedaMascota()
    
    return render (request,'ver_mascotas.html', {'mascotas': mascotas, 'formulario': formulario})
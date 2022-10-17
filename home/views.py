#from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.forms import Mascota, BusquedaMascota

def index (request):

    return render(request, 'index.html')

def alta_mascota(request):
    if request.method == 'POST':
        formulario = Mascota(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            duenio = data['duenio']
            edad = data['edad']
            fecha_ingreso = data['fecha_ingreso']
            if not fecha_ingreso:
                fecha_ingreso = datetime.now()
            
            mascota = Mascota(nombre=nombre, duenio=duenio, edad=edad, fecha_ingreso=fecha_ingreso)
            mascota.save()
            
            return redirect('ver_mascotas')
    formulario = Mascota()
    
    return render(request, 'alta_mascota.html', {'formulario': formulario})

def ver_mascotas(request):
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        mascotas = Mascota.objects.filter(nombre__icontains=nombre)
    else:
        mascotas = Mascota.objects.all()
        
    formulario = BusquedaMascota()
    
    return render (request,'ver_mascotas.html', {'mascotas': mascotas, 'formulario': formulario})
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.forms import FormMascota, BusquedaMascota
from home.models import Mascota

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index (request):

    return render(request, 'index.html')

# def alta_mascota(request):
#     if request.method == 'POST':
#         formulario = FormMascota(request.POST)
        
#         if formulario.is_valid():
#             data=formulario.cleaned_data

#             nombre=data['nombre']
#             duenio=data['duenio']
#             edad=data['edad']
                        
#             mascota = Mascota(nombre=nombre, duenio=duenio, edad=edad)
#             mascota.save()
            
#             return redirect('ver_mascotas')
#         else:
#                 return render(request, 'alta_mascota.html', {'formulario': formulario})
#     formulario = FormMascota()
    
#     return render(request, 'alta_mascota.html', {'formulario': formulario})

# def ver_mascotas(request):
#     nombre = request.GET.get('nombre', None)
    
#     if nombre:
#         mascotas = Mascota.objects.filter(nombre__icontains=nombre)
#     else:
#         mascotas = Mascota.objects.all()
        
#     formulario = BusquedaMascota()
    
#     return render (request,'ver_mascotas.html', {'mascotas': mascotas, 'formulario': formulario})

# def editar_mascota(request, id):
#     mascota = Mascota.objects.get(id=id)
    
#     if request.method == 'POST':
#         formulario = FormMascota(request.POST)
        
#         if formulario.is_valid():
#             data=formulario.cleaned_data

#             mascota.nombre=data['nombre'] #nombre=data['nombre']
#             mascota.duenio=data['duenio'] #duenio=data['duenio']
#             mascota.edad=data['edad'] #edad=data['edad']
#             mascota.save()
            
#             return redirect('ver_mascotas')
    
#     formulario = FormMascota(
#         initial={
#             'nombre' : mascota.nombre,
#             'duenio' : mascota.duenio,
#             'edad' : mascota.edad
#         }
#     )
#     return render(request, 'editar_mascota.html', {'formulario': formulario, 'mascota': mascota})

# def eliminar_mascota(request, id):
#     mascota = Mascota.objects.get(id=id)
#     mascota.delete()
#     return redirect ('ver_mascotas')

class VerMascotas(ListView):
    model = Mascota
    template_name = 'ver_mascotas_cbv.html'

class AltaMascota(CreateView):
    model = Mascota
    success_url= '/ver-mascotas' #Aqui puede haber algun error...
    template_name = 'alta_mascota_cbv.html'
    fields = ['nombre','duenio','edad']
    
class EditarMascota(UpdateView):
    model = Mascota
    success_url= '/ver-mascotas' #Aqui puede haber algun error...
    template_name = 'editar_mascota_cbv.html'
    fields = ['nombre','duenio','edad']
    
class EliminarMascota(DeleteView):
    model = Mascota
    success_url= '/ver-mascotas' #Aqui puede haber algun error...
    template_name = 'eliminar_mascota_cbv.html'
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.forms import FormMascota, BusquedaMascota
from home.models import Mascota

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index (request):

    return render(request, 'index.html')

def nosotrxs (request):

    return render(request, 'nosotrxs.html')

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
from django import forms

class Mascota(forms.Form):
     nombre = forms.CharField(max_length=30)
     duenio = forms.CharField(max_length=30)
     edad = forms.IntegerField()
     fecha_ingreso = forms.DateField(required=False)
     
class BusquedaMascota(forms.Form):
    nombre = forms.CharField(max_length=30)
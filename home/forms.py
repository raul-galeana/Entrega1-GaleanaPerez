from django import forms

class FormMascota(forms.Form):
    nombre = forms.CharField(max_length=30)
    duenio = forms.CharField(max_length=30)
    edad = forms.IntegerField()
     
class BusquedaMascota(forms.Form):
    nombre = forms.CharField(max_length=30)
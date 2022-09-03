from socket import fromshare
from django import forms

class PerroForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    raza = forms.CharField(max_length=50)
    edad = forms.IntegerField()

class GatoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    raza = forms.CharField(max_length=50)
    edad = forms.IntegerField()

class AnimalForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    animal_tipo = forms.CharField(max_length=50)
    edad = forms.IntegerField()
# forms.py
from django import forms

class CargarArchivoForm(forms.Form):
    archivo = forms.FileField()


class CargarArchivoEntrenamientoForm(forms.Form):
    archivo = forms.FileField()

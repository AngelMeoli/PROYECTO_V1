
from cProfile import label
from email.policy import default
from tkinter import Widget
from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Mascota2, usuario_solicitud

class usuario_solicitud_form(forms.ModelForm):
    class Meta:

        model =usuario_solicitud

        fields='__all__'


 
class mascota_form(forms.ModelForm):
    class Meta:
        model=Mascota2

        fields= [
            'id',
            'nombre_mascota',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels={
            'id_mascota':'Identificador Mascota',
            'nombre_mascota':'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada':'Edad Aproximada',
            'fecha_rescate': 'Fechad de Rescate',
            'persona': 'Adoptante',
            'vacuna':'Vacunas', 
        }
        widgets={
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_mascota':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate':forms.DateInput(attrs={'class':'form-control'}),
            'persona':forms.Select(attrs={'class':'form-control'}),
            'vacuna':forms.CheckboxSelectMultiple(),
        }

    

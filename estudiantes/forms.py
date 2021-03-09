# This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from django import forms
from .models import Evaluacion, Notas, Asistencia


class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tú correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea)

class EvaluacionForm(ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'
class NotasForm(ModelForm):
    class Meta:
        model = Notas
        fields = '__all__'

class AsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'

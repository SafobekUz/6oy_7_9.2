from django import forms
from .models import Tur, Gul

class TurForm(forms.ModelForm):
    class Meta:
        model = Tur
        fields = ['name']

class GulForm(forms.ModelForm):
    class Meta:
        model = Gul
        fields = ['tur', 'name', 'color']

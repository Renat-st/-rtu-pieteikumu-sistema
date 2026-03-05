from django import forms
from .models import Pieteikums

class PieteikumsForm(forms.ModelForm):
    class Meta:
        model = Pieteikums
        fields = '__all__'
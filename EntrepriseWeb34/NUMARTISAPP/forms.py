from django import forms
from .models import DemandeService1

class DemandeServiceForm(forms.ModelForm):
    class Meta:
        model = DemandeService1
        fields = '__all__'




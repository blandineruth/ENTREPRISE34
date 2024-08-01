from django.apps import AppConfig
# from .models import QuoteRequest
# from django import forms


class NumartisappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NUMARTISAPP'


# class QuoteRequest(forms.ModelForm):
    # class Meta:
    #     model = QuoteRequest
    #     fields = ['name', 'email', 'phone', 'service', 'special_note']
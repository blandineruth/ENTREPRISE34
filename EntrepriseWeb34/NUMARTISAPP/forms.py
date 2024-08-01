from django import forms
from .models import DemandeService1
from .models import EntrepriseArtisan
from .models import devis
from .models import UserLogin
from django.contrib.auth.models import User
from .models import CustomUser


class DemandeServiceForm(forms.ModelForm):
    class Meta:
        model = DemandeService1
        fields = '__all__'


class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = devis
        fields = ['name', 'email', 'phone', 'typeservice', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-0', 
                'placeholder': 'Votre nom', 
                'style': 'height: 55px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-0', 
                'placeholder': 'Votre Email', 
                'style': 'height: 55px;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control border-0', 
                'placeholder': 'Télephone', 
                'style': 'height: 55px;'
            }),
            'typeservice': forms.TextInput(attrs={
                'class': 'form-control border-0', 
                'style': 'height: 55px;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control border-0', 
                'placeholder': 'Special Note'
            })
        }


class EntrepriseArtisanForm(forms.ModelForm):
    class Meta:
        model = EntrepriseArtisan
        fields = [
            'nom_commercial', 'structure_juridique', 'adresse_mail_entreprise', 
            'secteur_activite',
            'numero_telephone_entreprise', 'adresse_entreprise', 
            'nom_prenom_artisan', 'adresse_mail_artisan',
            'numero_telephone_artisan', 'adresse_artisan', 'annees_experience',
            'fonction_dans_entreprise',
            'horaires_travail', 'photo_artisan'

        ]   
 
           
class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control border-green-600'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe', 'class': 'form-control border-green-600'}))


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'}))
    phone_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Numéro de téléphone'}))
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password_confirm', 'Les mots de passe ne correspondent pas')

        return cleaned_data
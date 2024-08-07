from django import forms
from .models import DemandeService1
from .models import EntrepriseArtisan
from .models import devis
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import ContactUser
from django.contrib.auth.forms import UserCreationForm

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
                'placeholder': 'Téléphone', 
                'style': 'height: 55px;'
            }),
            'typeservice': forms.Select(attrs={
                'class': 'form-control border-0',
                'style': 'height: 55px;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control border-0', 
                'placeholder': 'Special Note'
            })
        }
        
    TYPE_SERVICE_CHOICES = [
        ('nettoyage', 'Nettoyage à domicile'),
        ('mecanique', 'Mécanique'),
        ('menuiserie', 'Menuiserie'),
        # Ajoutez d'autres options ici
    ]

    typeservice = forms.ChoiceField(choices=TYPE_SERVICE_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control border-0',
        'style': 'height: 55px;'
    }))


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


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUser
        fields = ['name', 'email', 'phone_number', 'typeservice', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre Nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro'}),
            'typeservice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
        
        
        
class AuthUser(UserCreationForm):
    first_name = forms.EmailField(
        label="entrer un Nom",
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'first_name'}),
        #help_text="Required. 150 characters or fewer. Lettersand @/./+/-/_ only.",
    )
    
    last_name = forms.EmailField(
        label="entrer un Prenom",
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'last_name'}),
        #help_text="Required. 150 characters or fewer. Lettersand @/./+/-/_ only.",
    )
       
    email = forms.EmailField(
        label="entrer un email",
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'email'}),
        #help_text="Required. 150 characters or fewer. Lettersand @/./+/-/_ only.",
    )
    
    phone_number = forms.EmailField(
        label="entrer un Numero",
        required=True,
        widget=forms.NumberInput(attrs={'autocomplete': 'phone_number'}),
        #help_text="Required. 150 characters or fewer. Lettersand @/./+/-/_ only.",
    ) 
    password1 = forms.CharField(
        label="entrer un mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )

    password2 = forms.CharField(
        label="confirmation de mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )
    
    
#class meta pour personnaliser les chants du formulaire
class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields +("password1","password2")

def __init__(self, *args, **kwargs):
        super(AuthUser, self).__init__(*args, **kwargs)
        # Ajoutez le placeholder pour chaque champ ici
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.fields['email'].widget.attrs['placeholder'] = 'Adresse e-mail'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Entrer le numéro'
        self.fields['email'].widget.attrs['placeholder'] = 'Adresse e-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe '
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
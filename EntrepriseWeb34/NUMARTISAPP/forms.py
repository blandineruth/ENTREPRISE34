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
            'name': forms.TextInput(attrs={'class': 'form-control',
                                        'placeholder': 'Votre nom',
                                        'style': 'height: 55px;'}),
            
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                            'placeholder': 'Votre Email', 
                                            'style': 'height: 55px;' }),
            
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 
                                            'placeholder': 'Votre Numero', 
                                            'style': 'height: 55px;'}),
            
            'typeservice': forms.TextInput(attrs={'class': 'form-control', 
                                            'placeholder': 'Type de service', 
                                            'style': 'height: 55px;'}),
            
            'message': forms.Textarea(attrs={'class': 'form-control', 
                                              'placeholder': 'Votre Message', 
                                            'style': 'height: 55px;'}),
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
       
    )
    
    phone_number = forms.EmailField(
        label="entrer un Numero",
        required=True,
        widget=forms.NumberInput(attrs={'autocomplete': 'phone_number'}),
    
    ) 
    password1 = forms.CharField(
        label="entrer un mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )

    password2 = forms.CharField(
        label="confirmation de mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )
    

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


# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AuthUser(UserCreationForm):
    first_name = forms.CharField(
        label='Prénom',
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'first_name', 'placeholder': 'Entrer votre Prénom'}),
    )
    last_name = forms.CharField(
        label='Nom',
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'last_name', 'placeholder': 'Entrer votre Nom'}),
    )
    username = forms.CharField(
        label='Nom d’utilisateur',
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'username', 'placeholder': 'Nom d’utilisateur'}),
    )
    email = forms.EmailField(
        label='Adresse e-mail',
        required=True,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'placeholder': 'Adresse e-mail'}),
    )
    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Mot de passe'}),
    )
    password2 = forms.CharField(
        label='Confirmer le mot de passe',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Confirmer le mot de passe'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Ce nom d’utilisateur est déjà pris.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Cet email est déjà utilisé.')
        return email

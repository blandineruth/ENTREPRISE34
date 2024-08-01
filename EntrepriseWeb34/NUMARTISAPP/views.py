from django.shortcuts import render, redirect, HttpResponse
from NUMARTISAPP.models import DemandeService1
from django.http import JsonResponse
from .forms import QuoteRequestForm
from .forms import EntrepriseArtisanForm
from .forms import UserLoginForm  # Assurez-vous d'importer la classe UserLogin
from .models import UserLogin
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegistrationForm
from .models import CustomUser



# Create your views here.

def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'Services.html')


def contact(request):
    return render(request, 'contact.html')


def devis(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save() 
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = QuoteRequestForm()
    return render(request, 'devis.html', {'form': form})


def inscription(request):
    return render(request, 'inscription.html')


def commande1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        demande = request.POST.get('demande')
        delai = request.POST.get('delai')
        heure = request.POST.get('heure')
        print(name, demande, delai, heure)
        request.session['commande_data'] = {
            'name': name,
            'demande': demande,
            'delai': delai,
            'heure': heure
        }
        return redirect('commande2')
    return render(request, 'commande1.html')


def commande2(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        print(address, ville, email, tel)
        request.session['commande_data1'] = {
            'address': address,
            'ville': ville,
            'email': email,
            'tel': tel
        }

        # Récupérer les données stockées dans la session
        commande_data = request.session.get('commande_data')
        if not commande_data:
            # Si aucune donnée n'est trouvée dans la session, rediriger vers la première page
            return redirect('commande1')
        return redirect('commande3')
    return render(request, 'commande2.html')


def commande3(request):
    if request.method == 'POST':
        budget = request.POST.get('budget')
        availability = request.POST.get('availability')
        # Récupérer les données stockées dans la session
        commande_data = request.session.get('commande_data')
        commande_data1 = request.session.get('commande_data1')
        if not commande_data or not commande_data1:
            # Si aucune donnée n'est trouvée dans la session, rediriger vers la première page
            return redirect('commande1')
        # Déterminer le contact_info en fonction de la disponibilité
        contact_info = commande_data1['email'] if availability == 'oui' else commande_data1['tel']
        # Mettre à jour les données de la commande avec les informations de commande3
        commande_data.update(commande_data1)
        commande_data.update({
            'budget': budget,
            'availability': availability,
            'contact_info': contact_info
        })
        # Sauvegarder toutes les données dans la base de données
        commend = DemandeService1.objects.create(**commande_data)
        commend.save()
        # Nettoyer la session
        del request.session['commande_data']
        del request.session['commande_data1']
        return HttpResponse("Commande complétée avec succès!")
    return render(request, 'commande3.html')

    
def Apropos(request):
    return render(request, 'Apropos.html')


def EntrepriseArtisan(request):
    if request.method == 'POST':
        form = EntrepriseArtisanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'EntrepriseArtisan.html',
                          {'form': EntrepriseArtisanForm(), 'success': True})
    else:
        form = EntrepriseArtisanForm()
    return render(request, 'EntrepriseArtisan.html', {'form': form})

def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Vérifie que les champs ne sont pas vides
            if email and password:
                try:
                    # Rechercher l'utilisateur par l'email
                    user = CustomUser.objects.get(email=email)
                except CustomUser.DoesNotExist:
                    form.add_error(None, 'Identifiants invalides')
                    return render(request, 'User_login.html', {'form': form})

                # Authentifier l'utilisateur
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    auth_login(request, user)  # Connecter l'utilisateur
                    return redirect('index')  # Redirige vers la page d'accueil
                else:
                    form.add_error(None, 'Identifiants invalides')
    else:
        form = UserLoginForm()

    return render(request, 'User_login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            CustomUser.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            auth_login(request, user)
            return redirect('index')  # Redirige vers la page d'accueil après l'inscription
    else:
        form = RegistrationForm()

    return render(request, 'CustomUser.html', {'form': form})
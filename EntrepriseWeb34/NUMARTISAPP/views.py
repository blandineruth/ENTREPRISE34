from django.shortcuts import render, redirect, HttpResponse
from NUMARTISAPP.models import DemandeService1
from django.http import JsonResponse
from .forms import QuoteRequestForm
from .forms import EntrepriseArtisanForm
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from .models import Servicetype, Profil
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.generic import DetailView
from .models import SubscriptionPack
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import AuthUser


def inscription(request):
    try:
        if request.method == 'POST':
            form = AuthUser(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.instance.email = form.cleaned_data['email']
                user = form.save()
                print(f"Utilisateur créé : nom: {user.first_name} password :{user.password} email: {user.email} {user.last_name} username: {user.username}")
                messages.success(request, "Inscription réussie ! Vous pouvez maintenant vous connecter.")
                return redirect('connexion')
            else:
                messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
        else:
            form = AuthUser()
    except Exception as e:
        messages.error(request, f"Une erreur est survenue : {e}")
    
    return render(request, 'inscription.html', {'form': form})
# pour la connexion
def connexion(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(f'{username}, password {password}')
        if user is not None:
            login(request, user)
            messages.success(request, "Bienvenue sur la plate-forme Numartis !")
            return redirect('index')
        else:
            messages.error(request, "nom ou mot de passe incorect")
    return render(request, 'connexion.html')

@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')

def profil_client(request):
    return render(request, 'profil_client.html')

def modification(request):
    user = request.user  
    if request.method == 'POST':
        form = AuthUser(request.POST, instance=user)  
        if form.is_valid():
            form.save()
            messages.success(request, "Votre profil a été mis à jour avec succès.")
            return redirect('index')  
    else:
        form = AuthUser(instance=user)  
    
    return render(request, 'modification.html', {'form': form})

def subscription_packs_view(request):
    packs = SubscriptionPack.objects.all()
    return render(request, 'subscription_packs.html', {'packs': packs})


def index(request):
    return render(request, 'index.html')


def Reaction(request):
    return render(request, 'Reaction.html')


def profil_view(request):
    profiles = Profil.objects.all()  # Si vous avez plusieurs profils ou ajustez selon vos besoins
    return render(request, 'profil.html', {'profiles': profiles})

   
def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Envoyer un e-mail de confirmation
        send_mail(
            'Confirmation d\'inscription à notre Newsletter',
            'Merci de vous être inscrit à notre newsletter ! Nous vous tiendrons informé des dernières nouvelles.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Inscription réussie ! Vous allez recevoir un e-mail de confirmation.')
        return redirect('home')  # Redirige vers la page d'accueil ou une autre page
    return render(request, 'newsletter_signup.html')


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


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ContactUser')  # Rediriger vers une page de succès ou afficher un message de succès
    else:
        form = ContactForm()
    return render(request, 'ContactUser.html', {'form': form})


def services_view(request):
    service_type = request.GET.get('service_type', '')
    if service_type:
        services = Servicetype.objects.filter(service_type__icontains=service_type)
    else:
        services = Servicetype.objects.all()

    return render(request, 'services.html', {'services': services})


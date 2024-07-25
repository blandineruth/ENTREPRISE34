from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'Services.html')


def contact(request):
    return render(request, 'contact.html')


def devis(request):
    return render(request, 'devis.html')


def inscription(request):
    return render(request, 'inscription.html')


def connexion(request):
    return render(request, 'deconnexion.html')


def commande1(request):
    return render(request, 'commande1.html')


def commande2(request):
    return render(request, 'commande2.html')


def commande3(request):
    return render(request, 'commande3.html')


def PLATFORME(request):
    return render(request, 'PLATFORME.html')

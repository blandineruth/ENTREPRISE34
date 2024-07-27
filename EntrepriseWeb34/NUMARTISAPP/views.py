from django.shortcuts import render, redirect,HttpResponse
from NUMARTISAPP.models import DemandeService1

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
    return render(request, 'connexion.html')


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


def PLATFORME(request):
    return render(request, 'PLATFORME.html')


def Apropos(request):
    return render(request, 'Apropos.html')
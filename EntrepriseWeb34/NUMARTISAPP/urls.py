from django.urls import path
from .import views
from .views import contact_view
from .views import inscription
from .views import services_view
from django.conf.urls.static import static
from django.conf import settings
from .views import newsletter_signup

urlpatterns = [
    path("", views.index, name="index"),
    path("commande1/", views.commande1, name="commande1"),
    path("commande2/", views.commande2, name="commande2"),
    path("commande3/", views.commande3, name="commande3"),
    path("ContactUser/", views.contact_view, name="ContactUser"),
    path("inscription/", views.inscription, name="inscription"),
    path("connexion/", views.connexion, name="connexion"),
    path("services/", views.services_view, name="services"),
    path("devis/", views.devis, name="devis"),
    path("EntrepriseArtisan/", views.EntrepriseArtisan, name="EntrepriseArtisan"),
    path("Apropos/", views.Apropos, name="Apropos"),
    path('newsletter-signup/', newsletter_signup, name='newsletter_signup'),
    path('profil/', views.profil_view, name='profil'),
    path('subscription_packs/', views.subscription_packs_view, name='subscription_packs'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil_client/',views.profil_client,name='profil_client'),
    path('modification/',views.modification,name='modification'),
    path('Reaction/',views.Reaction,name='Reaction'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
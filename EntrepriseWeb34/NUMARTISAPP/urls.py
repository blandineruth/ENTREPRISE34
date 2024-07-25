from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("inscription/", views.inscription, name="inscription"),
    path("connexion/", views.connexion, name="connexion"),
    path("commande1/", views.commande1, name="commande1"),
    path("commande2/", views.commande2, name="commande2"),
    path("commande3/", views.commande3, name="commande3"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="Services"),
]

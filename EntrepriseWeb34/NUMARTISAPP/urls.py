from django.urls import path
from . import views
from .views import user_login_view
from .views import registration_view
from . views import contact_view


urlpatterns = [
    path("", views.index, name="index"),
    path("CustomUser/", views.registration_view, name="CustomUser"),
    path("User_login/", views.user_login_view, name="User_login"),
    path("commande1/", views.commande1, name="commande1"),
    path("commande2/", views.commande2, name="commande2"),
    path("commande3/", views.commande3, name="commande3"),
    path("contact/", views.contact_view, name="contact"),
    path("services/", views.services, name="services"),
    path("devis/", views.devis, name="devis"),
    path("EntrepriseArtisan/", views.EntrepriseArtisan, name="EntrepriseArtisan"),
    path("Apropos/", views.Apropos, name="Apropos"),

]

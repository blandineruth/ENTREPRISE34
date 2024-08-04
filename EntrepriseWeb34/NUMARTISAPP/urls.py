from django.urls import path
from . import views
from .views import user_login_view
from .views import registration_view
from .views import contact_view
from .views import services_view
from django.conf.urls.static import static
from django.conf import settings
from .views import newsletter_signup

urlpatterns = [
    path("", views.index, name="index"),
    path("CustomUser/", views.registration_view, name="CustomUser"),
    path("User_login/", views.user_login_view, name="User_login"),
    path("commande1/", views.commande1, name="commande1"),
    path("commande2/", views.commande2, name="commande2"),
    path("commande3/", views.commande3, name="commande3"),
    path("contact/", views.contact_view, name="contact"),
    path("services/", views.services_view, name="services"),
    path("devis/", views.devis, name="devis"),
    path("EntrepriseArtisan/", views.EntrepriseArtisan, name="EntrepriseArtisan"),
    path("Apropos/", views.Apropos, name="Apropos"),
    path('newsletter-signup/', newsletter_signup, name='newsletter_signup'),
    path('profil/', views.profil_view, name='profil'),
    path('subscription_packs/', views.subscription_packs_view, name='subscription_packs'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
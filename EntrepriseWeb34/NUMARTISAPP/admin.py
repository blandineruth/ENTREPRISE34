from django.contrib import admin
from .models import ContactUser, Carousel, Feature, About, Icon, DemandeService1, Servicetype, SubscriptionPack, Profil

# Enregistrement des modèles pour l'administration
admin.site.register(ContactUser)
admin.site.register(Carousel)
admin.site.register(Feature)
admin.site.register(About)
admin.site.register(Icon)
admin.site.register(DemandeService1)

@admin.register(Servicetype)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type')
    search_fields = ('name', 'service_type')
    list_filter = ('service_type',)

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'fonction', 'secteur_activite')

@admin.register(SubscriptionPack)
class SubscriptionPackAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')
    list_filter = ('price',)

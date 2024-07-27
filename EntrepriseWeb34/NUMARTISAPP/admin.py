from django.contrib import admin

# Register your models here.

from .models import ContactInfo, Carousel, Feature, About, Icon,DemandeService1

admin.site.register(ContactInfo)
admin.site.register(Carousel)
admin.site.register(Feature)
admin.site.register(About)
admin.site.register(Icon)
admin.site.register(DemandeService1)

from django.contrib import admin

# Register your models here.

from .models import ContactUser, Carousel, Feature, About, Icon, DemandeService1, ServiceFirst

admin.site.register(ContactUser)
admin.site.register(Carousel)
admin.site.register(Feature)
admin.site.register(About)
admin.site.register(Icon)
admin.site.register(DemandeService1)


@admin.register(ServiceFirst)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type')
    search_fields = ('name', 'service_type')
    list_filter = ('service_type',)


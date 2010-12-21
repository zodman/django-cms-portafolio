from django.contrib import admin
from plugins.cmsplugin_portafolio.models import Service, Client, Proyect, Image

class ImageInline(admin.TabularInline):
    model =Image

class ProyectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Proyect,ProyectAdmin)



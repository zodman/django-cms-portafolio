from django.contrib import admin
    
from django.db import models
from django.contrib import admin

from models import Service, Client, Proyect, Image, Country

from cms.plugins.text.widgets.wymeditor_widget import WYMEditor

class ImageInline(admin.TabularInline):
    model =Image

class ProyectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    formfield_overrides = {
        models.TextField : {'widget': WYMEditor},
    }
    list_display = ("name", "sequence",)
    list_editable = ( "sequence", )
    class Media:
        js = ("js/jquery-1.4.3.min.js",)


admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Country)
admin.site.register(Proyect,ProyectAdmin)


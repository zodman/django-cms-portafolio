from django.contrib import admin
from models import Opening, Candidate, EnableOpening, Require


class OpeAdmin(admin.ModelAdmin):
    raw_id_fields = ("require",)
    prepopulated_fields = {"slug": ("title",)}



class CandidatesInline(admin.TabularInline):
    model = Candidate
    extra = 1


class EnOpAdmin(admin.ModelAdmin):
    raw_id_fields = ("opening",)
    inlines = [CandidatesInline]
admin.site.register(Opening, OpeAdmin)
admin.site.register(Require)
admin.site.register(Candidate)
admin.site.register(EnableOpening, EnOpAdmin)

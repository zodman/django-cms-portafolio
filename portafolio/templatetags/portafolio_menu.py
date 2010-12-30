from django import template
from portafolio.models import Client

register = template.Library()

@register.inclusion_tag("portafolio/menu.html")
def portafolio_menu_client():
    return {"portafolio_clients":Client.objects.all()}

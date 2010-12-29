from django import template
from portafolio.models import Client

register = template.Library()

class PortafolioMenuNode(template.Node):
    def render(self, context):
        context["portafolio_clients"] = Client.objects.all()
        return ''
@register.tag
def portafolio_menu_client(parse, token):
    return PortafolioMenuNode()
    

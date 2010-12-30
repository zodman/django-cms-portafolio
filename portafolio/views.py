
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from models import Proyect



def index(request):
    p = Proyect.objects.all()[0]
    return direct_to_template(request, "portafolio/index.html", 
                              extra_context = { 'proyect':p })


def proyect(request, slug):
    p = get_object_or_404(Proyect, slug = slug)
    return direct_to_template(request, "portafolio/index.html", 
                              extra_context = { 'proyect':p })


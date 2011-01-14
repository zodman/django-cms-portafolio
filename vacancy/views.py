from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from models import EnableOpening, Opening

def index(request):
    eopen = EnableOpening.objects.all()
    d = {"opens": eopen}
    return direct_to_template(request,
            template="vacancy/index.html",
            extra_context = d,
            )

def detail(request, slug):
    qs = Opening.objects.all()
    d = {"queryset": qs, 
         "slug_field":"slug",
         "slug": slug,
        }
    return object_detail(request,**d)


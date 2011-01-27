from django.conf.urls.defaults import *

urlpatterns = patterns('portafolio.views',
    url(r"^$", "index", name="portafolio-index"),
    url(r"^(?P<slug>[-\w]+)/$", "proyect", name="portafolio-proyect"),
    url(r"^redirect/$", "redirect", name="portafolio-redirect"),
    url(r"^small/$", "show_small", name="portafolio-small"),
)


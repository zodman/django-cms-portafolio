from django.conf.urls.defaults import *

urlpatterns = patterns('portafolio.views',
    url(r"^$", "index", name="portafolio-index"),
    url(r"^(?P<slug>[-\w]+)$", "proyect", name="portafolio-proyect"),
)


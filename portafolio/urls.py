from django.conf.urls.defaults import *

urlpatterns = patterns('portafolio.views',
    url(r"^(P?<slug>[-\w]*)*$", "index", name="portafolio-index"),

)


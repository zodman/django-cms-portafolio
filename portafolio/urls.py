from django.conf.urls.defaults import *

urlpatterns = patterns('portafolio.views',
    url(r"^(P?<slug>[-\w]i*)*$", "index", name="portafolio-index"),

)


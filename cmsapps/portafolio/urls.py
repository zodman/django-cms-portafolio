from django.conf.urls.defaults import *

urlpatterns = patterns("cmsapps.portafolio.views", 
        url(r"^$", "index", name="portafolio-index"),                  
    )

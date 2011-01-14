from django.conf.urls.defaults import *

urlpatterns = patterns("vacancy.views",
    url(r"^$", 'index', name="vacancy-index"),
)

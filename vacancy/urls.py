from django.conf.urls.defaults import *
from models import Opening

urlpatterns = patterns("vacancy.views",
     url(r"^detail/(?P<slug>[-\w]+)/$", 'detail',name="job-detail"),
   url(r"^$", 'index', name="vacancy-index"),
)

from django.conf.urls.defaults import *
from models import Opening

urlpatterns = patterns("vacancy.views",
     url(r"^detail/(?P<id>\d+)/$", 'detail',name="job-detail"),
     url(r"^apply/(?P<id>\d+)/$", 'show_form',name="show-form"),
     url(r"^$", 'index', name="vacancy-index"),
)

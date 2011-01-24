from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
     (r'^admin/', include(admin.site.urls)),
     (r'^fb/', 'vacancy.views.facebook')
)


if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^media/cms/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CMS_MEDIA_ROOT, 'show_indexes': True}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)

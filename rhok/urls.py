from django.conf.urls.defaults import *

urlpatterns = patterns('rhok.views',
    url(r'^$', 'index', name='rhok-index')
)

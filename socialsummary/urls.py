from django.conf.urls.defaults import patterns, url, include
from views import *

urlpatterns = patterns('',
    url(r'twitter', twitter),
    url(r'$', home),
)

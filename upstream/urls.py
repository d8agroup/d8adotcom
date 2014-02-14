from django.conf.urls.defaults import patterns, url, include
from views import *

urlpatterns = patterns('',
    url(r'about$', about),	
	url(r'solutions$', solutions),
    url(r'$', home),
)
from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
	url(r'about$', about),
	url(r'partners$', partners),
	url(r'press$', press),	
	url(r'$', home),
)
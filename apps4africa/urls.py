from django.conf.urls.defaults import patterns, url, include
from views import *

urlpatterns = patterns('',
    url(r'about$', about),
    url(r'team$', team),
    url(r'events$', events),
    url(r'press$', press),
	url(r'partners$', partners),
	url(r'video$', video),
    url(r'contact$', contact),
	url(r'program$', program),
	url(r'portfolio$', portfolio),
    url(r'eir$', eir),
	url(r'challenge$', challenge),	
    url(r'$', home),
)

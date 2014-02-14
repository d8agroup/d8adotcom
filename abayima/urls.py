from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
	url(r'about$', about),
	url(r'team$', team),
	url(r'partners$', partners),
	url(r'press$', press),
	url(r'faq$', faq),
	url(r'research$', research),
	url(r'community$', community),
	url(r'contact$', contact),
	url(r'resources$', resources),
	url(r'history$', history),
	url(r'donate$', donate),	
	url(r'$', home),
)
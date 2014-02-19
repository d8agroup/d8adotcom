from django.conf.urls.defaults import patterns, url
from d8a import views

urlpatterns = patterns(
    '',
    url(r'about$', views.about, name='d8a_about'),
    url(r'contact$', views.contact, name='d8a_contact'),
    url(r'projects$', views.projects, name='d8a_projects'),
	url(r'products$', views.products, name='d8a_products'),
	url(r'resources$', views.resources, name='d8a_resources'),
    url(r'clients$', views.clients, name='d8a_clients'),
	url(r'initiatives$', views.initiatives, name='initiatives'),
    url(r'capabilities$', views.capabilities, name='d8a_capabilities'),
    url(r'solutions/global$', views.solutions_global, name='d8a_solutions_global'),
    url(r'solutions/data$', views.solutions_data, name='d8a_solutions_data'),
    url(r'solutions/civic_engagement$', views.solutions_civic_engagement, name='d8a_solutions_service_delivery'),
    url(r'solutions$', views.solutions_all, name='d8a_solutions_all'),
    url(r'$', views.home, name='d8a_home'),
)
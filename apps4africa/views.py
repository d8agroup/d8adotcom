from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return render_to_response(
        'apps4africa/home.html',
        {},
        context_instance=RequestContext(request)
    )

def about(request):
    return render_to_response(
        'apps4africa/about.html',
        {},
        context_instance=RequestContext(request)
    )

def team(request):
    return render_to_response(
        'apps4africa/team.html',
        {},
        context_instance=RequestContext(request)
    )

def events(request):
    return render_to_response(
        'apps4africa/events.html',
        {},
        context_instance=RequestContext(request)
    )
	
def press(request):
    return render_to_response(
        'apps4africa/press.html',
        {},
        context_instance=RequestContext(request)
    )

def video(request):
	    return render_to_response(
	        'apps4africa/video.html',
	        {},
	        context_instance=RequestContext(request)
	    )

def contact(request):
    return render_to_response(
        'apps4africa/contact.html',
        {},
        context_instance=RequestContext(request)
    )

def portfolio(request):
    return render_to_response(
        'apps4africa/portfolio.html',
        {},
        context_instance=RequestContext(request)
    )

def eir(request):
    return render_to_response(
        'apps4africa/eir.html',
        {},
        context_instance=RequestContext(request)
    )
	
def challenge(request):
    return render_to_response(
        'apps4africa/challenge.html',
        {},
        context_instance=RequestContext(request)
    )

def partners(request):
    return render_to_response(
        'apps4africa/partners.html',
        {},
        context_instance=RequestContext(request)
    )

def program(request):
	return render_to_response(
	    'apps4africa/program.html',
	    {},
	    context_instance=RequestContext(request)
	)

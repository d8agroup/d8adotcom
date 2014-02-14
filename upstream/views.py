from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return render_to_response(
        'upstream/home.html',
        {},
        context_instance=RequestContext(request)
    )

def about(request):
    return render_to_response(
        'upstream/about.html',
        {},
        context_instance=RequestContext(request)
    )

def solutions(request):
    return render_to_response(
        'upstream/solutions.html',
        {},
        context_instance=RequestContext(request)
    )
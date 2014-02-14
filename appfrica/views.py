from django.contrib import messages
from django.contrib.messages.constants import INFO
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return render_to_response(
        'appfrica/home.html',
        {},
        context_instance=RequestContext(request)
    )

def stat(request):
    return render_to_response(
        'appfrica/s/stat.html',
        {},
        context_instance=RequestContext(request)
    )

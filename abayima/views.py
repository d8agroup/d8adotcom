from django.contrib import messages
from django.contrib.messages.constants import INFO
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return render_to_response(
        'abayima/home.html',
        {},
        context_instance=RequestContext(request)
    )
def about(request):
    return render_to_response(
        'abayima/about.html',
        {},
        context_instance=RequestContext(request)
    )
def partners(request):
    return render_to_response(
        'abayima/partners.html',
        {},
        context_instance=RequestContext(request)
    )
def team(request):
    return render_to_response(
        'abayima/team.html',
        {},
        context_instance=RequestContext(request)
    )
def research(request):
	return render_to_response(
	    'abayima/research.html',
	    {},
	    context_instance=RequestContext(request)
	)
def faq(request):
	return render_to_response(
	    'abayima/faq.html',
	    {},
	    context_instance=RequestContext(request)
	    )
def press(request):
	return render_to_response(
	    'abayima/press.html',
	    {},
	    context_instance=RequestContext(request)
	   )
def community(request):
	return render_to_response(
	    'abayima/community.html',
	    {},
	    context_instance=RequestContext(request)
	)
def resources(request):
	return render_to_response(
	    'abayima/resources.html',
	    {},
	    context_instance=RequestContext(request)
	)	
def history(request):
	return render_to_response(
	    'abayima/history.html',
	    {},
	    context_instance=RequestContext(request)
	)
def donate(request):
	return render_to_response(
	    'abayima/donate.html',
	    {},
	    context_instance=RequestContext(request)
	)			
def contact(request):
    message_sent = False
    if request.method == 'POST':
        sender_name = request.POST.get('senderName', 'NO NAME GIVEN')
        sender_email = request.POST.get('senderEmail', 'NO EMAIL GIVEN')
        message = request.POST.get('message', 'NO MESSAGE GIVEN')
        message = 'FROM: %s \nEMAIL: %s \nMESSAGE: %s' % (sender_name, sender_email, message)
        send_mail('Contact request from the Abayima.com site', message, sender_email, ['info@abayima.com'], fail_silently=True)
        message_sent = True
    return render_to_response(
	    'abayima/contact.html',
	    { 'message_sent':message_sent },
	    context_instance=RequestContext(request)
	)
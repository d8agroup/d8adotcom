from django.core.mail import send_mail
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext


def old_home(request):
    if request.GET.get('next', 'false') == 'true':
        return redirect(home)
    message_sent = False
    if request.method == 'POST':
        first_name = request.POST.get('first_name', 'NO NAME GIVEN')
        last_name = request.POST.get('last_name', 'NO NAME GIVEN')
        sender_email = request.POST.get('email', 'NO EMAIL GIVEN')
        sender_phone = request.POST.get('phone', 'NO PHONE GIVEN')
        subject = request.POST.get('subject', 'NO SUBJECT GIVEN')
        message = request.POST.get('message', 'NO MESSAGE GIVEN')
        message = 'FROM: %s, %s \nEMAIL: %s \nPHONE: %s \nSUBJECT: %s \nMESSAGE: %s' % (
            first_name, last_name, sender_email, sender_phone, subject, message)
        send_mail('Contact request from the d8a.com site', message, sender_email, ['info@d8a.com'], fail_silently=True)
        message_sent = True
    return render_to_response(
        'd8a/home.html',
        {'message_sent': message_sent}, context_instance=RequestContext(request))


def home(request):
    return render_to_response('d8a/home.html', context_instance=RequestContext(request))

def solutions_all(request):
    return render_to_response('d8a/solutions.html', context_instance=RequestContext(request))

def solutions_data(request):
    return render_to_response('d8a/solutions_data.html', context_instance=RequestContext(request))

def solutions_civic_engagement(request):
    return render_to_response('d8a/solutions_civic_engagement.html', context_instance=RequestContext(request))

def solutions_global(request):
    return render_to_response('d8a/solutions_global.html', context_instance=RequestContext(request))

def projects(request):
    return render_to_response('d8a/projects.html', context_instance=RequestContext(request))

def products(request):
    return render_to_response('d8a/products.html', context_instance=RequestContext(request))

def clients(request):
    return render_to_response('d8a/clients.html', context_instance=RequestContext(request))

def capabilities(request):
    return render_to_response('d8a/capabilities.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('d8a/about.html', context_instance=RequestContext(request))

def initiatives(request):
    return render_to_response('d8a/initiatives.html', context_instance=RequestContext(request))

def contact(request):
    return render_to_response('d8a/contact.html', context_instance=RequestContext(request))

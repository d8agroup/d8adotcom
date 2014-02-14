from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson as json
from utils import get_sentiment
import urllib

def home(request):
    template_data = { 'keyword':request.GET.get('keyword') }
    return render_to_response('socialsummary/home.html', template_data, context_instance=RequestContext(request))

def twitter(request):
    results = urllib.urlopen("http://search.twitter.com/search.json?rpp=100&q="+request.GET.get('keyword'))
    results = json.loads(results.read())

    template_data = {
        'raw':results,
        'accounts':{},
        'sentiment':{ 'raw':{} },
        'velocity':{ 'raw':{} }
    }
    for tweet in results['results']:
        user_id = tweet['from_user_id']

        #Top contributing accounts
        if user_id not in template_data['accounts']:
            template_data['accounts'][user_id] = {
                'profile_image':tweet['profile_image_url'],
                'username':tweet['from_user_name'],
                'count':0
            }
        template_data['accounts'][user_id]['count'] += 1

        #Sentiment
        text = tweet['text']
        sentiment = get_sentiment(text)
        if sentiment not in template_data['sentiment']['raw']:
            template_data['sentiment']['raw'][sentiment] = 0
        template_data['sentiment']['raw'][sentiment] +=1

    template_data['accounts'] = sorted(template_data['accounts'].values(), key=lambda a: a['count'], reverse=True)[:18]
    template_data['sentiment']['labels'] = template_data['sentiment']['raw'].keys()
    template_data['sentiment']['data'] = template_data['sentiment']['raw'].values()
    template_data['template'] = render_to_string('socialsummary/twitter.html', template_data)
    return HttpResponse(json.dumps(template_data), content_type='application/json')
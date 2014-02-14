import datetime
from django import template
import re

register = template.Library()
 
@register.filter("truncate_chars")
def truncate_chars(value, max_length):
    if len(value) <= max_length:
        return value
 
    truncd_val = value[:max_length]
    #if value[max_length] != " ":
        #rightmost_space = truncd_val.rfind(" ")
        #if rightmost_space != -1:
            #truncd_val = truncd_val[:rightmost_space]
 
    return truncd_val + "..."

@register.filter('is_url')
def is_url(value):
    return re.search('http', value)

@register.filter('is_in')
def is_in(value, list):
    return value in list

@register.filter('is_true')
def is_true(value):
    return value == True or value == 'True'

@register.filter('datetime_to_hours_ago')
def datetime_to_hours_ago(value):
    time_delta = (datetime.datetime.now() - value)
    time_delta = divmod(time_delta.days * 86400 + time_delta.seconds, 60)
    hours = int(float(time_delta[0])/60)
    if not hours:
        return 'now'
    return '%i hours ago' % hours

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

@register.filter('strip')
def sub(value, pattern):
    return re.sub(pattern, '', value)
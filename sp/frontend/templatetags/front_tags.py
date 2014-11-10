from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='get_range')
def get_range(value):
    return [i for i in range(int(value))]
    
@register.filter(name='linebreaksli')
def linebreaksli(value):
    lines = value.split('\n')
    newlines = [u'<li>%s</li>' % line.strip() for line in lines if len(line.strip()) > 0 ]
    return mark_safe(u''.join(newlines))    
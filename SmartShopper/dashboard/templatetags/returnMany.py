from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="returnMany")
def returnMany(object):
    return object.all()
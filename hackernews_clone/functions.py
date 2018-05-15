from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
@register.simple_tag  
@stringfilter
def default_color_label():
    default_label = ColorLabels.objects.filter(default=True).first()
    return default_label
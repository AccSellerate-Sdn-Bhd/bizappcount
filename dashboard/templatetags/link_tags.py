from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.inclusion_tag('imports.html')
def imports():
    return {}
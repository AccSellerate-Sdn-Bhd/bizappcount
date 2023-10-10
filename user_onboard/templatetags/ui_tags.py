from django import template
from django.template.loader import render_to_string
from django.contrib.auth import logout

register = template.Library()


@register.inclusion_tag('header.html')
def header(user):
    return {'user': user}


@register.inclusion_tag('sidebar_template.html')
def sidebar_template(url, request):
    return {'url': url}

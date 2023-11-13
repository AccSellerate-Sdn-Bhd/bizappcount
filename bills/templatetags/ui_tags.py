from django import template
from django.template.loader import render_to_string
from django.contrib.auth import logout

register = template.Library()


@register.inclusion_tag('header.html')
def header(user):
    return {'user': user}


@register.inclusion_tag('sidebar_template.html')
def sidebar_template(url, request):
    def logoutFunction():
        logout(request)

    return {'url': url, 'function': logoutFunction}


@register.inclusion_tag('dashboard_tab.html')
def dashboard_tab(title, subtitle, text_color):
    return {'title': title, 'subtitle': subtitle, 'text_color': text_color}


@register.inclusion_tag('warning_tab.html')
def warning_tab(title, subtitle):
    return {'title': title, 'subtitle': subtitle}

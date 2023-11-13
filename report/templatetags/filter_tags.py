from django import template

register = template.Library()

@register.filter
def get_item_name(data, index):
    try:
        return data[index].account.name
    except (IndexError, KeyError):
        return None

@register.filter
def get_item_amount(data, index):
    try:
        return data[index].amount
    except (IndexError, KeyError):
        return None

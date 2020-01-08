from django import template

register = template.Library()

@register.filter
def even(value):
    return value % 2 == 0
        
from django import template

register = template.Library()


@register.filter
def replace(value, arg):
    replace_from, replace_to = arg.split(":")
    return value.replace(replace_from, replace_to)

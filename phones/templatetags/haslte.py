from django import template


register = template.Library()

@register.filter
def haslte(val):
    if val:
        return 'Да'
    else:
        return 'Нет'

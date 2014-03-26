from django import template

register = template.Library()

@register.filter(name='incrementSept')
def increment(value, plusPlus):
	return plusPlus + 7

@register.filter(name='incrementHuit')
def increment(value, plusPlus):
	return plusPlus + 8
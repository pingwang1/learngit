from django import template

register = template.Library()



#1.
def percent(value):
	return str(value)+"%"
register.filter(percent)



#2.
@register.filter(name=percent)
def percent(value):
	return str(value)+"%"
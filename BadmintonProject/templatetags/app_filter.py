from django import template
import time
register = template.Library()
@register.filter(name='convertDate')
def convertDate(valueDate):
    if valueDate:
        return valueDate.strftime("%Y-%m-%d")

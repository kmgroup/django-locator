from django.template.loader import render_to_string
from django.template import Library
from django.template import RequestContext


register = Library()


@register.simple_tag
def locator():
    return render_to_string('locator/templatetags/locator.html')

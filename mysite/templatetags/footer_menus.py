from django import template
from django.template.defaultfilters import stringfilter
from wagtailmenus.models import FlatMenu
register = template.Library()

@register.simple_tag
def footer_menus():
    return FlatMenu.objects.all()

# filter(handle__endswith='footer')
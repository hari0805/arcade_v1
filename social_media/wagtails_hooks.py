from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import SocialMediaSettings

class ApplicationAdmin(ModelAdmin):
    model = SocialMediaSettings
    menu_icon = 'chain-broken'
    menu_order = 400
    list_display = ('name', 'url')

modeladmin_register(ApplicationAdmin)
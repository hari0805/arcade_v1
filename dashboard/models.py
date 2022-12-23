from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

@register_setting(icon='cog')
class CustomBrandSettings(BaseSiteSetting):
    favicon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    logo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    welcome_message = models.CharField(
        max_length=30, null=True, blank=True, 
        help_text='Your Welcome message'
    )
    login_message = models.CharField(
        max_length=30, null=True, blank=True,
        help_text='Your Login message'
    )

    panels = [
            FieldPanel("favicon"),
            FieldPanel("logo"),
            FieldPanel("welcome_message"),
            FieldPanel("login_message"),
        ]

    class Meta:
        verbose_name = 'Custom branding'




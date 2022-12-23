from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.core.models import Orderable
from modelcluster.models import ClusterableModel

from modelcluster.fields import ParentalKey


@register_setting(icon='media')
class SocialMediaSettings(ClusterableModel, BaseSiteSetting):

    panels = [
        MultiFieldPanel([
            InlinePanel('Social_Media', label="Name & URL"),
        ], heading="Social Media accounts")
        
    ]

    class Meta:
        verbose_name = 'social media'

class SocialMediaNameUrl(Orderable):

    page = ParentalKey("social_media.SocialMediaSettings", related_name="Social_Media")
    name = models.CharField(
        max_length=255, help_text='Your Social media name, like instagram, facebook....')
    url = models.URLField(
        help_text='Your user account URL')

    panels = [
        MultiFieldPanel([
            FieldPanel("name"),
            FieldPanel("url"),
        ])
        
    ]
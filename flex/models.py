"""Flexible page."""
from django.db import models
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class FlexPage(Page):
    """Flexibile page class."""

    template = "flex/flex_page.html"

    # @todo add streamfields 
    # content = StreamField()

    subtitle = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:  # noqa 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

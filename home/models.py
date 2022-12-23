from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    banner_panels = [
        MultiFieldPanel(
            [
               FieldPanel('body', classname="full"), 
            ],
            heading="Banner Options",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            # This is our custom banner_panels. It's just a list, how easy!
            ObjectList(banner_panels, heading="Banner Settings"),
            ObjectList(Page.promote_panels, heading='Promotional Stuff'),
            ObjectList(Page.settings_panels, heading='Settings Stuff'),
        ]
    )

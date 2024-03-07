from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class LandingPage(Page):
    introduction = RichTextField(blank=True)
    body = RichTextField(blank=True)
    # Add more fields as needed, such as images, links to social media, etc.

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        FieldPanel('body', classname="full"),
        # Add more panels as needed for additional fields
    ]

    # You can add methods here for company-specific logic, such as fetching dynamic content


class CompanyPage(Page):
    introduction = RichTextField(blank=True)
    body = RichTextField(blank=True)
    # Add more fields as needed, such as images, links to social media, etc.

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        FieldPanel('body', classname="full"),
        # Add more panels as needed for additional fields
    ]

    # You can add methods here for company-specific logic, such as fetching dynamic content


class ContactPage(Page):
    introduction = RichTextField(blank=True)
    body = RichTextField(blank=True)
    # Add more fields as needed, such as images, links to social media, etc.

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        FieldPanel('body', classname="full"),
        # Add more panels as needed for additional fields
    ]

    # You can add methods here for company-specific logic, such as fetching dynamic content

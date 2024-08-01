from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Collection
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)


class HomePage(Page):
    parent_page_types = [
        'wagtailcore.Page'
    ]
    child_page_types = [
        'blog.BlogIndexPage',
        'company.CompanyIndexPage',
        'contact.ContactPage',
        'inventory.UserInventoryIndex'
    ]

    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    hero_heading = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("hero heading")
    )
    hero_body = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("hero body")
    )
    primary_cta_url = models.URLField(
        null=True,
        blank=True
    )
    primary_cta_text = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    secondary_cta_url = models.URLField(
        null=True,
        blank=True
    )
    secondary_cta_text = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def get_hero_content(self):
        return {
            'heading': self.hero_heading if self.hero_heading else 'No Heading',
            'body': self.hero_body if self.hero_body else 'No Body',
            'primary_url': self.primary_cta_url if self.primary_cta_url else '#',
            'primary_text': self.primary_cta_text if self.primary_cta_text else 'Get Started',
            'secondary_url': self.secondary_cta_url if self.secondary_cta_url else '#',
            'secondary_text': self.secondary_cta_text if self.secondary_cta_text else 'Learn More'
        }

    def get_context(self, request):
        context = super().get_context(request)
        context['hero'] = self.get_hero_content()
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_heading'),
                FieldPanel('hero_body'),
                FieldRowPanel(
                    [
                        FieldPanel('primary_cta_url'),
                        FieldPanel('primary_cta_text'),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel('secondary_cta_url'),
                        FieldPanel('secondary_cta_text'),
                    ]
                ),
            ],
            heading="Hero Body"
        ),
        FieldPanel('collection'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('homepage')

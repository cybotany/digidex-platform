from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel


class InventoryIndexPage(Page):
    parent_page_types = [
        'home.HomePage'
    ]
    child_page_types = [
        'inventory.UserInventoryPage'
    ]

    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    intro = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )

    def get_body_header(self):
        return {
            'title': self.title,
            'intro': self.intro if self.intro else 'Need to add an intro'
        }

    def get_context(self, request):
        context = super().get_context(request)
        userpages = self.get_children().live().order_by('-first_published_at')
        context['header'] = self.get_body_header()
        context['userpages'] = userpages

        return context

    content_panels = Page.content_panels + [
        FieldPanel('collection'),
        FieldPanel('intro')
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('inventory index page')

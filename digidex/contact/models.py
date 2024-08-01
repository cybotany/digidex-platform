from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel


class ContactPage(AbstractEmailForm):
    intro = models.CharField(
        max_length=255,
        blank=True
    )
    form_subtitle = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Form subtitle'
    )
    form_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Form title'
    )

    def get_body_header(self):
        return {
            'title': self.title,
            'intro': self.intro if self.intro else 'Needs to be defined'
        }

    def get_form_info(self):
        return {
            'subtitle': self.form_subtitle if self.form_subtitle else 'Contact us',
            'heading': self.form_title if self.form_title else 'Submit your message',
        }

    def get_context(self, request):
        context = super().get_context(request)
        context['header'] = self.get_body_header()
        context['info'] = self.get_form_info()
        return context

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        MultiFieldPanel(
            [
                FieldPanel('form_subtitle'),
                FieldPanel('form_title'),
                InlinePanel('form_fields', label="Form fields"),
            ],
            heading="Form"
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('from_address'),
                        FieldPanel('to_address'),
                    ]
                ),
                FieldPanel('subject'),
            ],
            heading="Email"
        ),

    ]


class ContactField(AbstractFormField):
    page = ParentalKey(
        ContactPage,
        on_delete=models.CASCADE,
        related_name='form_fields'
    )

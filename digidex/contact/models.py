from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel


class ContactPage(AbstractEmailForm):
    intro = models.CharField(
        max_length=255,
        blank=True
    )
    thank_you_text = RichTextField(
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

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
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
            heading="Email"),
    ]


class ContactField(AbstractFormField):
    page = ParentalKey(
        ContactPage,
        on_delete=models.CASCADE,
        related_name='form_fields'
    )

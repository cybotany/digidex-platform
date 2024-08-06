from django.db import models
from django.forms import widgets

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

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="Form fields"),
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

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for name, field in form.fields.items():
            if isinstance(field.widget, widgets.Input):
                field.widget.attrs.update({'class': 'text-field w-input'})
            if isinstance(field.widget, widgets.Textarea):
                field.widget.attrs.update({'class': 'text-field textarea'})       
        return form


class ContactField(AbstractFormField):
    page = ParentalKey(
        ContactPage,
        on_delete=models.CASCADE,
        related_name='form_fields'
    )

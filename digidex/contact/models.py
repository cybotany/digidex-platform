from django.db import models
from django.forms import widgets

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel


class ContactPage(AbstractEmailForm):
    parent_page_types = ['home.HomePage']
    child_page_types = []

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        InlinePanel('contact_form_fields', label="Form fields"),
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

    def get_form_fields(self):
        return self.contact_form_fields.all()


class ContactField(AbstractFormField):
    page = ParentalKey(
        ContactPage,
        on_delete=models.CASCADE,
        related_name='contact_form_fields'
    )

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FormSubmissionsPanel
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

class ContactField(AbstractFormField):
    """
    Defines a field for the contact form. This can be extended to include additional
    fields specific to your contact form requirements.
    """
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='contact_fields'
    )

class ContactPage(AbstractEmailForm):
    """
    The ContactPage model represents a contact form page in the Wagtail site. It includes
    an introduction, a customizable thank you text, and dynamically generated form fields.
    """
    intro = RichTextField(
        blank=True,
        default="Welcome to our contact form! Please fill out the form below with your questions or comments."
    )
    thank_you_text = RichTextField(
        blank=True,
        default="Thank you for reaching out to us! We will get back to you as soon as possible."
    )

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('contact_fields', label="Contact fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldPanel('from_address'),
            FieldPanel('to_address'),
            FieldPanel('subject'),
        ], heading="Email Settings"),
    ]

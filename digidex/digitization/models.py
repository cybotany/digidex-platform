import uuid

from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

from modelcluster.fields import ParentalKey

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel


class DigitizedObject(models.Model):
    """
    Base class for digitized objects, providing common attributes.

    Attributes:
        name (CharField): The name of the digitized object.
        uuid (UUIDField): The unique identifier for the digitized object.
        description (RichTextField): A detailed description of the digitized object.
        created_at (DateTimeField): The date and time the digitized object was created.
        last_modified (DateTimeField): The date and time the digitized object was last modified.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False
    )
    description = RichTextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )


class DigitizedObjectRegistrationField(AbstractFormField):
    page = ParentalKey(
        'digitization.DigitizedObjectRegistrationPage',
        on_delete=models.CASCADE,
        related_name='form_fields'
    )


class DigitizedObjectRegistrationPage(AbstractForm):
    intro = RichTextField(
        blank=True
    )
    thank_you_text = RichTextField(
        blank=True
    )

    content_panels = AbstractForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Digit Fields"),
        FieldPanel('thank_you_text'),
    ]

    def process_form_submission(self, form):
        digitized_object = DigitizedObject(
            name=form.cleaned_data['name'],
            description=form.cleaned_data.get('description', '')
        )
        digitized_object.save()
        return redirect(reverse('thank-you'))

    def serve(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')
        ntag_id = request.GET.get('ntag_id')
        form_context = {
            'user_id': user_id,
            'ntag_id': ntag_id
        }
        return super().serve(request, *args, **kwargs, extra_context=form_context)

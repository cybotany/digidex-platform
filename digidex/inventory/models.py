import uuid

from django.db import models
from django.conf import settings
from django.utils.text import slugify

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, PublishingPanel, PageChooserPanel
from wagtail.search import index

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel


class UserIndexPage(Page):
    body = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    subpage_types = ['inventory.UserPage']


class UserPage(Page):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="user_pages"
    )

    search_fields = Page.search_fields + [
        index.SearchField('get_username', partial_match=True, boost=2),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('user'),
    ]

    subpage_types = ['inventory.DigitPage']

    def get_username(self):
        """Method to return the username of the associated user."""
        return self.user.username

    def get_biography(self):
        """Method to return the biography of the associated user."""
        return self.user.biography

    class Meta:
        verbose_name = "User Profile Page"


class Digit(Orderable):
    user = ParentalKey(
        'UserPage',
        null=True,
        on_delete=models.CASCADE,
        related_name='digits'
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False
    )
    slug = models.SlugField(
        null=True,
        db_index=True,
        verbose_name="Digit Slug"
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digit UUID"
    )
    description = RichTextField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
            original_slug = self.slug
            count = 1

            while Digit.objects.filter(page=self.page, slug=self.slug).exists():
                self.slug = f'{original_slug}-{count}'
                count += 1

        super(Digit, self).save(*args, **kwargs)


class DigitFormField(AbstractFormField):
    page = ParentalKey(
        'DigitRegistrationFormPage',
        on_delete=models.CASCADE,
        related_name='form_fields'
    )


class DigitRegistrationFormPage(AbstractEmailForm):
    intro = RichTextField(
        blank=True
    )
    thank_you_text = RichTextField(
        blank=True
    )

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Digit Fields"),
        FieldPanel('thank_you_text'),
    ]

    def process_form_submission(self, form):
        # Create a Digit instance from the form data
        digit = Digit(
            user=form.cleaned_data.get('user'),
            name=form.cleaned_data['name']
        )
        digit.save()

        digit_page = DigitPage(
            title=digit.name,
            digit=digit,
            user=form.cleaned_data.get('user_page')  # Assume a UserPage instance is provided
        )
        self.add_child(instance=digit_page)
        digit_page.save_revision().publish()

        return super().process_form_submission(form)


class DigitPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'DigitPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class DigitPage(Page):
    digit = models.ForeignKey(
        Digit,
        on_delete=models.PROTECT,
        related_name='pages'
    )
    user = models.ForeignKey(
        UserPage,
        on_delete=models.PROTECT,
        related_name='digit_pages'
    )
    tags = ClusterTaggableManager(
        through=DigitPageTag,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified"
    )

    search_fields = Page.search_fields + [
        index.SearchField('get_digit_name', partial_match=True, boost=2),
        index.SearchField('get_digit_description', partial_match=True, boost=2),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                PageChooserPanel('user'),
                FieldPanel('tags'),
            ],
            heading="Digit Metadata"
        ),
        FieldPanel('digit'),
        InlinePanel('digit_images', label="Digit images"),
    ]

    def get_main_image(self):
        digit_item = self.digit_images.first()
        if digit_item:
            return digit_item.image
        else:
            return None

    def get_digit_name(self):
        """Method to return the name of the digitized object."""
        return self.digit.name

    def get_digit_description(self):
        """Method to return the description of the digitized object."""
        return self.digit.description

    def save(self, *args, **kwargs):
        if not self.pk:
            base_slug = slugify(self.digit.name)
            self.slug = base_slug
            count = 1

            while DigitPage.objects.filter(slug=self.slug, user=self.user).exists():
                self.slug = f'{base_slug}-{count}'
                count += 1

        super(DigitPage, self).save(*args, **kwargs)


class DigitPageGalleryImage(Orderable):
    page = ParentalKey(
        DigitPage,
        on_delete=models.CASCADE,
        related_name='digit_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(
        blank=True,
        max_length=250
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class DigitTagIndexPage(Page):
    def get_context(self, request):
        tag = request.GET.get('tag')
        digitpages = DigitPage.objects.filter(tags__name=tag)
        context = super().get_context(request)
        context['digitpages'] = digitpages
        return context

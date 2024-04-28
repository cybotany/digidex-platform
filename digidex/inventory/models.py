import uuid
from django.db import models, transaction
from django.conf import settings

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, ImageChooserPanel, PageChooserPanel


class UserProfileIndexPage(Page):
    intro = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    subpage_types = ['inventory.UserProfilePage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        profiles = self.get_children().live().order_by('title')
        context['profiles'] = profiles
        return context


class UserProfilePage(Page):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile_pages"
    )
    avatar = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    biography = models.TextField(
        max_length=500,
        blank=True,
        help_text='A short biography of the user.'
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        help_text='The location of the user.'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('avatar'),
        FieldPanel('biography'),
        FieldPanel('location')
    ]

    subpage_types = ['inventory.UserDigitPage']


class UserDigit(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digit UUID"
    )
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )
    ntag = models.OneToOneField(
        'nfc.NearFieldCommunicationTag',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='%(class)s'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified"
    )

    @classmethod
    def create_digit(cls, form_data, link, user):
        with transaction.atomic():    
            digit = cls.objects.create(
                ntag=link,
                **form_data
            )
            link.user = user
            link.active = True
            link.save()

            return digit

    def delete(self, *args, **kwargs):
        """
        Overrides the delete method of the model to include custom deletion logic.
        """
        if self.ntag:
            self.ntag.reset_to_default()
            self.ntag.save()
        super(UserDigit, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class UserDigitPage(Page):
    digit = models.ForeignKey(
        UserDigit,
        on_delete=models.CASCADE,
        related_name='pages'
    )
    owner = models.ForeignKey(
        UserProfilePage,
        on_delete=models.CASCADE,
        related_name='items'
    )

    content_panels = Page.content_panels + [
        FieldPanel('digit'),
        PageChooserPanel('owner'),
    ]

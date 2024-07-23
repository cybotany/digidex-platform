from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import (
    Page,
    Collection,
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from wagtail.fields import RichTextField
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.snippets.models import register_snippet

class DigiDexImage(AbstractImage):
    caption = models.TextField(
        blank=True,
        null=True,
        max_length=150
    )
    alt_text = models.CharField(
        blank=True,
        null=True,
        max_length=75
    )

    admin_form_fields = Image.admin_form_fields + (
        'caption',
        'alt_text',
    )


class DigiDexRendition(AbstractRendition):
    image = models.ForeignKey(
        DigiDexImage,
        on_delete=models.CASCADE,
        related_name='renditions'
    )

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )


@register_snippet
class DigiDexLogo(models.Model):
    logo = models.ForeignKey(
        get_image_model(),
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel("logo"),
    ]

    def __str__(self):
        return "DigiDex Logo"

    class Meta:
        verbose_name = "Site Logo"
        verbose_name_plural = "Site Logos"


@register_snippet
class DigiDexFooterParagraph(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    paragraph = models.TextField(
        max_length=100
    )

    panels = [
        FieldPanel("paragraph"),
    ]

    def __str__(self):
        return "Footer Text"

    def get_preview_template(self, request, mode_name):
        return "index.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_paragraph": self.paragraph}

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Footer Paragraph"
        verbose_name_plural = "Footer Paragraphs"


@register_snippet
class DigiDexFooterCopyright(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    copyright = models.TextField(
        max_length=100
    )

    panels = [
        FieldPanel("copyright"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer Copyright"

    def get_preview_template(self, request, mode_name):
        return "index.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_copyright": self.copyright}

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Footer Copyright"
        verbose_name_plural = "Footer Copyrights"


class AbstractDigiDexPage(Page):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    body = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("body")
    )

    content_panels = Page.content_panels + [
        FieldPanel('collection'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    class Meta:
        abstract = True

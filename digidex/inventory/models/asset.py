import uuid

from django.db import models, transaction
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Collection, Orderable
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path


class InventoryAssetPage(RoutablePageMixin, Page):
    RESERVED_KEYWORDS = ['add', 'update', 'delete', 'admin']

    parent_page_types = ['inventory.UserInventoryPage']
    child_page_types = ['inventory.AssetFormPage']

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("name")
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("description")
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['is_owner'] = self.is_owner(request.user)
        context['asset'] = self
        context['parent'] = self.get_parent()
        context['edit_url'] = self.reverse_subpage('edit')
        return context

    def set_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def get_parent_collection(self):
        parent = self.get_parent().specific
        return parent.collection

    def create_collection(self):
        parent = self.get_parent_collection()
        uuid = str(self.uuid)
        children = parent.get_children()
        try:
            collection = children.get(name=uuid)
        except Collection.DoesNotExist:
            collection = parent.add_child(name=uuid)
        return collection

    @transaction.atomic
    def set_collection(self):
        self.collection = self.create_collection()

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    @property
    def main_image(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def is_owner(self, user):
        return user == self.owner

    @path('edit/', name='edit')
    def edit(self, request):
        if request.user != self.owner:
            raise PermissionDenied

        from inventory.forms import InventoryAssetForm
        if request.method == "POST":
            form = InventoryAssetForm(request.POST, instance=self)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(self.url)
        else:
            form = InventoryAssetForm(instance=self)
        
        return self.render(
            request,
            template='inventory/includes/edit_asset.html',
            context_overrides={
                'form': form,
                'show_decoupling_checkbox': hasattr(self, 'linked_tag')
            }
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.set_slug()
        if not self.collection:
            self.set_collection()
        if self.name and self.name.lower() in self.RESERVED_KEYWORDS:
            raise ValueError(f"The name '{self.name}' is reserved and cannot be used.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("user inventory asset")
        verbose_name_plural = _("user inventory assets")


class AssetJournalEntry(ClusterableModel):
    page = models.ForeignKey(
        InventoryAssetPage,
        on_delete=models.deletion.CASCADE,
        related_name='+'
    )
    date = models.DateField(
        verbose_name="Journal Entry Date"
    )
    note = RichTextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('note'),
        InlinePanel('gallery_documents', label="Gallery documents"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class JournalGalleryDocument(Orderable):
    journal_entry = ParentalKey(
        AssetJournalEntry,
        on_delete=models.deletion.CASCADE,
        related_name='gallery_documents'
    )
    document = models.ForeignKey(
        get_document_model(),
        on_delete=models.deletion.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('document'),
    ]


class JournalGalleryImage(Orderable):
    journal_entry = ParentalKey(
        AssetJournalEntry,
        on_delete=models.deletion.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        get_image_model(),
        on_delete=models.deletion.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]

import uuid

from django.db import models, transaction
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Collection
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path


class InventoryAssetPage(RoutablePageMixin, Page):
    RESERVED_KEYWORDS = ['add', 'edit', 'delete', 'admin']

    parent_page_types = ['inventory.UserInventoryPage']
    child_page_types = []

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
    taxon_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Taxonomy Identifier")
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
        InlinePanel('journal_entries', label="Journal entries"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        entries = self.journal_entries.all().order_by('-created_at')
        context['entries'] = entries
        context['is_owner'] = self.is_owner(request.user)
        context['asset'] = self
        context['urls'] = self.get_urls()
        return context

    def get_urls(self):
        return {
            'edit': self.reverse_subpage('edit'),
            'parent': self.get_parent().url,
        }

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


import uuid

from django.db import models, transaction
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.models import Page, Collection, Site


class InventoryAssetPage(RoutablePageMixin, Page):
    parent_page_types = [
        'inventory.UserInventoryPage'
    ]

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("name")
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("description")
    )
    body = RichTextField(
        null=True,
        blank=True,
        verbose_name=_("body")
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    RESERVED_KEYWORDS = ['add', 'update', 'delete', 'admin']

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

    @path('update/')
    def update_inventory(self, request):
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
            template='inventory/includes/update_asset.html',
            context_overrides={'form': form}
        )

    @path('delete/')
    def delete_inventory(self, request):
        if request.user != self.owner:
            raise PermissionDenied

        from inventory.forms import DeletionConfirmationForm
        if request.method == "POST":
            form = DeletionConfirmationForm(request.POST)
            if form.is_valid():
                self.delete()
                site = Site.find_for_request(request)
                if site is not None:
                    home_page_url = site.root_page.url
                else:
                    home_page_url = reverse('/')
                return HttpResponseRedirect(home_page_url)
        else:
            form = DeletionConfirmationForm()
        
        return self.render(
            request,
            template='inventory/includes/delete_asset.html',
            context_overrides={'form': form}
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

import uuid

from django.db import models, transaction
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.models import Page, Collection, Site


class UserInventoryIndex(RoutablePageMixin, Page):
    parent_page_types = [
        'home.HomePage'
    ]
    child_page_types = [
        'inventory.UserInventoryAsset'
    ]

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
        related_name='+',
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    def create_slug(self):
        if self.owner:
            return slugify(self.owner.username)
        return slugify(self.title)

    def set_slug(self):
        self.slug = self.create_slug()

    def get_parent_collection(self):
        parent = Collection.get_first_root_node()
        parent_children = parent.get_children()
        try:
            collection = parent_children.get(name='Inventory')
        except Collection.DoesNotExist:
            collection = parent.add_child(name="Inventory")
        return collection

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

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    @path('update/')
    def update_inventory(self, request):
        if request.user != self.owner:
            raise PermissionDenied

        from inventory.forms import UserInventoryForm
        if request.method == "POST":
            form = UserInventoryForm(request.POST, instance=self)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(self.url)
        else:
            form = UserInventoryForm(instance=self)
        
        return self.render(
            request,
            template='inventory/forms/update_index.html',
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
            template='inventory/forms/delete_index.html',
            context_overrides={'form': form}
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.set_slug()
        if not self.collection:
            self.set_collection()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('user inventory')

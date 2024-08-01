import uuid

from django.db import models, transaction
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.models import Page, Collection, Site


class UserInventoryPage(RoutablePageMixin, Page):
    parent_page_types = [
        'inventory.InventoryIndexPage'
    ]
    child_page_types = [
        'inventory.InventoryAssetPage'
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
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def get_context(self, request):
        context = super().get_context(request)
        assets = self.get_children().live().order_by('-first_published_at')
        context['is_owner'] = self.is_owner(request.user)
        context['assets'] = assets
        context['urls'] = self.get_page_urls()
        return context

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

    @property
    def main_image(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def is_owner(self, user):
        return user == self.owner

    def get_page_urls(self):
        return {
            'detail': self.url,
            'add': self.reverse_subpage('add'),
            'update': self.reverse_subpage('update'),
            'delete': self.reverse_subpage('delete'),
        }

    @path('add/', name='add')
    def add_asset(self, request):
        if request.user != self.owner:
            raise PermissionDenied

        from inventory.forms import InventoryAssetForm
        from inventory.models import InventoryAssetPage

        if request.method == "POST":
            form = InventoryAssetForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                asset = InventoryAssetPage(
                    title=name,
                    slug=slugify(name),
                    owner=self.owner,
                    name=name,
                    description=description
                )
                self.add_child(instance=asset)
                asset.save_revision().publish()
                return redirect(asset.url)
        else:
            form = InventoryAssetForm()
        
        return self.render(
            request,
            template='inventory/includes/add_asset.html',
            context_overrides={'form': form}
        )

    @path('update/', name='update')
    def update_inventory(self, request):
        if request.user != self.owner:
            raise PermissionDenied

        from inventory.forms import UserInventoryForm
        if request.method == "POST":
            form = UserInventoryForm(request.POST)
            if form.is_valid():
                self.description = form.cleaned_data['description']
                self.save()
                return redirect(self.url)
        else:
            form = UserInventoryForm(initial={'description': self.description})
        
        return self.render(
            request,
            template='inventory/includes/update_index.html',
            context_overrides={'form': form}
        )

    @path('delete/', name='delete')
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
                return redirect(home_page_url)
        else:
            form = DeletionConfirmationForm()
        
        return self.render(
            request,
            template='inventory/includes/delete_index.html',
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

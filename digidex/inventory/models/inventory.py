import uuid

from django.db import models, transaction
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.models import Page, Collection
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class TrainerInventoryPage(RoutablePageMixin, Page):
    parent_page_types = [
        'inventory.InventoryIndexPage'
    ]
    child_page_types = [
        'inventory.InventoryAssetPage'
    ]

    trainer = models.OneToOneField(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='page'
    )
    collection = models.OneToOneField(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )
    description = RichTextField(
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('trainer'),
        FieldPanel('collection'),
        FieldPanel('description'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        assets = self.get_children().live().order_by('-first_published_at')
        context['is_owner'] = self.is_owner(request.user)
        context['assets'] = assets
        context['urls'] = self.get_page_urls()
        return context

    def create_slug(self):
        return slugify(self.trainer.username)

    def set_slug(self):
        self.slug = self.create_slug()

    def get_parent_collection(self):
        parent = Collection.get_first_root_node()
        parent_children = parent.get_children()
        try:
            collection = parent_children.get(name='Trainers')
        except Collection.DoesNotExist:
            collection = parent.add_child(name="Trainers")
        return collection

    @transaction.atomic
    def create_collection(self):
        parent = self.get_parent_collection()
        uuid = str(self.trainer.uuid)
        children = parent.get_children()
        try:
            trainer_collection = children.get(name=uuid)
        except Collection.DoesNotExist:
            trainer_collection = parent.add_child(name=uuid)
        return trainer_collection

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
        return user == self.trainer

    def get_page_urls(self):
        return {
            'detail': self.url,
            'add': self.reverse_subpage('add'),
            'edit': self.reverse_subpage('edit'),
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

    @path('edit/', name='edit')
    def edit_inventory(self, request):
        if request.user != self.owner:
            raise PermissionDenied

        from inventory.forms import TrainerInventoryForm
        if request.method == "POST":
            form = TrainerInventoryForm(request.POST)
            if form.is_valid():
                self.description = form.cleaned_data['description']
                self.save()
                return redirect(self.url)
        else:
            form = TrainerInventoryForm(initial={'description': self.description})
        
        return self.render(
            request,
            template='inventory/includes/edit_inventory.html',
            context_overrides={'form': form}
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.set_slug()
        if not self.collection:
            self.collection = self.create_collection()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.trainer.__str__()}'s page"

    class Meta:
        verbose_name = _('trainer page')
        verbose_name_plural = _('trainer pages')


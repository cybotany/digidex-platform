import uuid

from django.db import models
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils.text import slugify

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images import get_image_model
from wagtail.api import APIField
from wagtail.models import Collection, Page
from wagtail.admin.panels import FieldPanel

from .forms  import InventoryForm, DeleteInventoryForm, InventoryAssetForm


CustomImageModel = get_image_model()

class InventoryPage(RoutablePageMixin, Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory UUID"
    )
    collection = models.ForeignKey(
        Collection,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    parent_page_types = [
        'trainer.TrainerPage'
    ]

    subpage_types = [
        'asset.AssetPage'
    ]

    api_fields = [
        APIField('uuid'),
        APIField('description'),
    ]

    def get_main_image(self):
        #entry = self.journal_entries.order_by('-created_at').first()
        #if entry:
        #    return entry.image
        return None

    def get_formatted_date(self):
        if self.live:
            return self.first_published_at.strftime('%B %d, %Y')
        return "Draft"

    def get_formatted_title(self):
        return self.title.title()

    @route(r'^update/$', name='update_inventory_view')
    def update_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed here.")

        if request.method == 'POST':
            form = InventoryForm(request.POST)
            if form.is_valid():
                if 'title' in form.cleaned_data:
                    title = form.cleaned_data['title']
                    self.title = title
                    self.slug = slugify(title)
                if 'description' in form.cleaned_data:
                    self.description = form.cleaned_data['description']
                self.save()
                messages.success(request, 'Category successfully updated')
                return redirect(self.url)
        else:
            initial_data = {
                'title': self.title,
                'description': self.description
            }
            form = InventoryForm(initial=initial_data)

        return render(request, 'inventory/includes/update_form.html', {'form': form})

    @route(r'^delete/$', 'delete_inventory_view')
    def delete_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed here.")

        if request.method == 'POST':
            form = DeleteInventoryForm(request.POST)
            if form.is_valid():
                parent_page = self.get_parent()
                self.delete()
                messages.success(request, 'Category successfully deleted')
                return redirect(parent_page.url)
        else:
            form = DeleteInventoryForm()

        return render(request, 'inventory/includes/delete_form.html', {'form': form})

    @route(r'^add/$', name='add_asset_view')
    def add_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed here.")
        
        if request.method == 'POST':
            form = InventoryAssetForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                asset_page = apps.get_model('asset', 'assetpage')(
                    title=title.title(),
                    slug=slugify(title),
                    owner=page_owner,
                    description=form.cleaned_data['description']
                )
                self.add_child(instance=asset_page)
                asset_page.save_revision().publish()
                messages.success(request, f'{title} successfully added!')
                return redirect(asset_page.url)
        else:
            form = InventoryAssetForm()
        
        return render(request, 'inventory/includes/asset_form.html', {'form': form})

    def get_page_heading(self):
        return {
            'title': self.get_formatted_title(),
            'date': self.get_formatted_date(),
            'paragraph': self.description,
            'update_url': self.reverse_subpage('update_inventory_view'),
            'delete_url': self.reverse_subpage('delete_inventory_view'),
        }

    def get_asset_collection(self):
        AssetPage = apps.get_model('asset', 'assetpage')
        assets = self.get_children().type(AssetPage).live().specific()
        collection = [asset.get_card() for asset in assets]
        return collection

    def get_card(self):
        return {
            'uuid': self.uuid,
            'title': self.title,
            'url': self.url,
            'icon': None
        }

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['page_heading'] = self.get_page_heading()
        context['asset_collection'] = self.get_asset_collection()
        return context

    class Meta:
        verbose_name = "Inventory Category Page"

    def __str__(self):
        return f"Inventory: {self.title}"

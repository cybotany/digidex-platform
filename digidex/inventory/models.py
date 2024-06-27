import uuid

from django.db import models
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseForbidden
from django.utils.text import slugify

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images import get_image_model
from wagtail.api import APIField
from wagtail.models import Collection, Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from .forms  import InventoryForm, DeleteInventoryForm


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
    description = RichTextField(
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

    def get_main_image(self):
        #entry = self.journal_entries.order_by('-created_at').first()
        #if entry:
        #    return entry.image
        return None

    def get_formatted_date(self):
        return 'DraftDate'

    def get_formatted_title(self):
        return self.title.title()

    @route(r'^update/$', name='update_inventory_view')
    def update_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

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

        return render(request, 'inventory/category/update.html', {'form': form, 'url': self.url})

    @route(r'^delete/$', 'delete_inventory_view')
    def delete_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = DeleteInventoryForm(request.POST)
            if form.is_valid():
                parent_page = self.get_parent()
                self.delete()
                messages.success(request, 'Category successfully deleted')
                return redirect(parent_page.url)
        else:
            form = DeleteInventoryForm()

        return render(request, 'inventory/category/delete.html', {'form': form, 'url': self.url})

    def get_page_heading(self):
        return {
            'title': self.get_formatted_title(),
            'paragraph': self.description,
        }

    def get_asset_collection(self):
        _type = ContentType.objects.get(app_label='asset', model='assetpage')
        _collection = self.get_children().filter(content_type=_type)
        _assets = [_asset.specific.get_summary() for _asset in _collection]
        _default = _assets[0]
        asset_section = {
            'title': 'Assets',
            'collection': _collection,
            'default': _default,
        }
        return asset_section

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['page_heading'] = self.get_page_heading()
        context['asset_collection'] = self.get_asset_collection()
        return context

    class Meta:
        verbose_name = "Inventory Category Page"

    def __str__(self):
        return f"Inventory: {self.title}"

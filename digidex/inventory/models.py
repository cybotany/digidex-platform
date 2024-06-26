import uuid

from django.db import models
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils.text import slugify

from modelcluster.fields import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images import get_image_model
from wagtail.api import APIField
from wagtail.models import Collection, Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from nfc.models import NearFieldCommunicationLink
from journal.models import Note, NoteImageGallery

from .forms  import InventoryForm, DeleteInventoryForm, InventoryournalEntryForm


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
    name = models.CharField(
        max_length=50
    )
    description = RichTextField(
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
    ]

    parent_page_types = [
        'trainer.TrainerPage'
    ]

    subpage_types = [
        'asset.AssetPage'
    ]

    @property
    def formatted_date(self):
        return self.first_published_at.strftime('%B %d, %Y')
    
    @property
    def formatted_name(self):
        return self.name.title()

    @route(r'^update/$', name='update_category_view')
    def update_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = InventoryForm(request.POST)
            if form.is_valid():
                if 'name' in form.cleaned_data:
                    name = form.cleaned_data['name']
                    self.name = name
                    self.slug = slugify(name)
                if 'description' in form.cleaned_data:
                    self.description = form.cleaned_data['description']
                self.save()
                messages.success(request, 'Category successfully updated')
                return redirect(self.url)
        else:
            initial_data = {
                'name': self.name,
                'description': self.description
            }
            form = InventoryForm(initial=initial_data)

        return render(request, 'inventory/category/update.html', {'form': form, 'url': self.url})

    @route(r'^delete/$', 'delete_category_view')
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

    def get_card_details(self):
        return {
            'name': self.formatted_name,
            'image': None,
            'date': self.formatted_date,
            'description': self.description or 'No description available',
            'detail_url': self.url,
        }

    def get_panel(self):
        return {
            'name': self.formatted_name,
            'image': None,
            'date': self.formatted_date, 
            'description': self.description or 'No description available',
            'update_url': self.reverse_subpage('update_category_view'),
            'delete_url': self.reverse_subpage('delete_category_view'),
        }

    def get_cards(self):
        cards = self.get_children()
        return cards

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['page_panel'] = self.get_panel()
        context['page_cards'] = self.get_cards()
        return context

    class Meta:
        verbose_name = "Inventory Category Page"

    def __str__(self):
        return f"Inventory: {self.name}"


class InventoryNote(Orderable, Note):
    inventory = ParentalKey(
        InventoryPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    panels = Note.panels + [
        InlinePanel('gallery_images', label="Note Image Gallery"),
    ]

    def __str__(self):
        return f"Inventory Journal Entry {self.uuid}"


class InventoryNoteImageGallery(NoteImageGallery):
    note = ParentalKey(
        InventoryNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )


class InventoryNearFieldCommunicationLink(NearFieldCommunicationLink):
    inventory = models.OneToOneField(
        InventoryPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    def __str__(self):
        return f"Inventory NFC: {self.uuid}"

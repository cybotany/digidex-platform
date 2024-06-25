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

from .forms import AssetForm, DeleteAssetForm, AssetJournalEntryForm


CustomImageModel = get_image_model()

class AssetPage(RoutablePageMixin, Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
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

    api_fields = [
        APIField('uuid'),
        APIField('name'),
        APIField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        InlinePanel('notes', label="Longitudinal Asset Notes"),
    ]

    parent_page_types = [
        'trainer.TrainerPage',
    ]

    subpage_types = []

    @property
    def image(self):
        return self.get_main_image()

    def get_main_image(self):
        entry = self.journal_entries.order_by('-created_at').first()
        if entry:
            return entry.image
        return None

    @property
    def formatted_date(self):
        return self.first_published_at.strftime('%B %d, %Y')
    
    @property
    def formatted_name(self):
        return self.name.title()

    @route(r'^update/$', name='update_digit_view')
    def update_digit_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not authorized to update this digital object.")
        
        if request.method == 'POST':
            form = AssetForm(request.POST, request.FILES)
            if form.is_valid():
                if 'name' in form.cleaned_data:
                    self.name = form.cleaned_data['name']
                if 'description' in form.cleaned_data:
                    self.description = form.cleaned_data['description']
                self.save()
                messages.success(request, 'Digital object successfully updated')
                return redirect(self.url)
        else:
            initial_data = {
                'name': self.name,
                'description': self.description
            }
            form = AssetForm(initial=initial_data)
        
        return render(request, 'inventory/digit/update.html', {'form': form})

    @route(r'^delete/$', 'delete_digit_view')
    def delete_digit_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not authorized to update this digital object.")

        if request.method == 'POST':
            form = DeleteAssetForm(request.POST)
            if form.is_valid():
                parent_page = self.get_parent()
                self.delete()
                messages.success(request, 'Digit successfully deleted')
                return redirect(parent_page.url)
        else:
            form = DeleteAssetForm()
        
        return render(request, 'inventory/digit/delete.html', {'form': form})

    @route(r'^add/$', name='add_digit_entry_view')
    def add_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to update this page.")
        
        if request.method == 'POST':
            form = AssetJournalEntryForm(request.POST, request.FILES)
            if form.is_valid():
                image_file = form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')
                note = form.cleaned_data.get('note')

                # Create the Wagtail Image object
                image = None
                if image_file:
                    image = CustomImageModel(
                        title=image_file.name,
                        file=image_file,
                        caption=caption,
                        collection=self.collection
                    )
                    image.save()
                journal_entry = AssetNote(
                    page=self,
                    image=image,
                    note=note,
                )
                journal_entry.save()
                messages.success(request, 'Journal entry successfully added.')
                return redirect(self.url)
        else:
            form = AssetJournalEntryForm()
        
        return render(request, 'inventory/digit/journal.html', {'form': form})

    def get_card_details(self):
        return {
            'name': self.formatted_name,
            'image': self.image,
            'date': self.formatted_date,
            'description': self.description or 'No description available',
            'detail_url': self.url,
        }

    def get_cards(self):
        if hasattr(self, 'journal_entries'):
            cards = self.journal_entries.all()
            return cards
        return []

    def get_panel(self):
        return {
            'name': self.formatted_name,
            'image': self.image,
            'date': self.formatted_date, 
            'description': self.description,
            'update_url': self.reverse_subpage('update_digit_view'),
            'delete_url': self.reverse_subpage('delete_digit_view'),
        }

    def get_tabs(self):
        return {
            'descendants': [],
            'add_url': self.reverse_subpage('add_digit_entry_view'),
            'form_model': 'Journal Entry',
        }

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['page_panel'] = self.get_panel()
        context['page_tabs'] = self.get_tabs()
        context['page_cards'] = self.get_cards()
        return context

    def __str__(self):
        return f"Asset: {self.name}"


class AssetNote(Note):
    asset = models.ForeignKey(
        AssetPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Asset Note: {self.uuid}"


class AssetNoteImageGallery(NoteImageGallery):
    note = ParentalKey(
        AssetNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    panels = NoteImageGallery.panels +  [
        InlinePanel('gallery_images', label="Note Image Gallery"),
    ]


class AssetNearFieldCommunicationLink(NearFieldCommunicationLink):
    asset = models.OneToOneField(
        AssetPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    def __str__(self):
        return f"Asset NFC: {self.uuid}"

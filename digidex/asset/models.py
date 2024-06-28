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

from .forms import AssetForm, DeleteAssetForm


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
    description = models.TextField(
        blank=True,
        null=True
    )

    api_fields = [
        APIField('uuid'),
        APIField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    parent_page_types = [
        'inventory.InventoryPage',
        'trainer.TrainerPage',
    ]

    subpage_types = []

    def get_main_image(self):
        #entry = self.journal_entries.order_by('-created_at').first()
        #if entry:
        #    return entry.image
        return None

    def get_formatted_date(self):
        return 'DraftDate'

    def get_formatted_title(self):
        return self.title.title()

    @route(r'^update/$', name='update_asset_view')
    def update_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not authorized to update this digital object.")
        
        if request.method == 'POST':
            form = AssetForm(request.POST, request.FILES)
            if form.is_valid():
                if 'title' in form.cleaned_data:
                    self.title = form.cleaned_data['title']
                if 'description' in form.cleaned_data:
                    self.description = form.cleaned_data['description']
                self.save()
                messages.success(request, 'Digital object successfully updated')
                return redirect(self.url)
        else:
            initial_data = {
                'title': self.title,
                'description': self.description
            }
            form = AssetForm(initial=initial_data)
        
        return render(request, 'asset/includes/update_form.html', {'form': form})

    @route(r'^delete/$', 'delete_asset_view')
    def delete_view(self, request):
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
        
        return render(request, 'asset/includes/delete_form.html', {'form': form})

    @route(r'^add/$', name='add_digit_entry_view')
    def add_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to update this page.")

        from journal.forms import JournalEntryForm
        if request.method == 'POST':
            form = JournalEntryForm(request.POST, request.FILES)
            if form.is_valid():
                note = form.save(commit=False)
                note.content_object = self
                note.collection = self.collection
                note.save()
                form.save_m2m()
                messages.success(request, 'Journal entry successfully added.')
                return redirect(self.url)
        else:
            form = JournalEntryForm()
        
        return render(request, 'asset/includes/journal_form.html', {'form': form})

    def get_page_heading(self):
        return {
            'title': self.get_formatted_title(),
            'paragraph': self.description,
            'update_url': self.reverse_subpage('update_asset_view'),
            'delete_url': self.reverse_subpage('delete_asset_view'),
        }

    def get_summary(self):
        return {
            'uuid': self.uuid,
            'title': self.get_formatted_title(),
            'description': self.description,
            'date': self.get_formatted_date(),
            'detail_url': self.url,
            'image': self.get_main_image(),
        }

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['page_heading'] = self.get_page_heading()
        return context

    class Meta:
        verbose_name = "Digitized Asset Page"

    def __str__(self):
        return f"Asset: {self.get_formatted_title()}"
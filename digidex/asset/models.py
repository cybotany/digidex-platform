import uuid

from django.db import models
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseForbidden

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images import get_image_model
from wagtail.api import APIField
from wagtail.models import Collection, Page
from wagtail.admin.panels import FieldPanel

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

    def get_formatted_date(self):
        if self.live:
            return self.first_published_at.strftime('%B %d, %Y')
        return "Draft"

    def get_formatted_title(self):
        return self.title.title()

    def get_journal_entries(self, order_by='-created_at'):
        content_type = ContentType.objects.get_for_model(self)
        JournalEntry = apps.get_model('journal', 'journalentry')
        return JournalEntry.objects.filter(content_type=content_type, object_id=self.id).order_by(order_by)

    def get_main_image(self):
        entries = self.get_journal_entries()
        image = entries[0].image if entries else None
        return image

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
                messages.success(request, 'Asset successfully deleted')
                return redirect(parent_page.url)
        else:
            form = DeleteAssetForm()
        
        return render(request, 'asset/includes/delete_form.html', {'form': form})

    @route(r'^add/$', name='add_journal_entry_view')
    def add_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to update this page.")

        JournalEntry = apps.get_model('journal', 'journalentry')

        if request.method == 'POST':
            form = AssetJournalEntryForm(request.POST, request.FILES)
            if form.is_valid():
                image_file = form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')
                entry = form.cleaned_data.get('entry')

                image = None
                if image_file:
                    image = CustomImageModel(
                        title=image_file.name,
                        file=image_file,
                        caption=caption,
                        collection=self.collection
                    )
                    image.save()
                journal_entry = JournalEntry(
                    content_object=self,
                    image=image,
                    entry=entry,
                )
                journal_entry.save()
                messages.success(request, 'Journal entry successfully added.')
                return redirect(self.url)
        else:
            form = AssetJournalEntryForm()
        
        return render(request, 'journal/includes/test_form.html', {'form': form})

    def get_heading_section(self):
        return {
            'title': self.get_formatted_title(),
            'date': self.get_formatted_date(),
            'paragraph': self.description,
            'update_url': self.reverse_subpage('update_asset_view'),
            'delete_url': self.reverse_subpage('delete_asset_view'),
        }

    def get_journal_section(self):
        entries = self.get_journal_entries()
        collection = [entry.get_card() for entry in entries]
        add_url = self.reverse_subpage('add_journal_entry_view')
        return {
            'title': 'Journal',
            'collection': collection,
            'add': add_url,
        }

    def get_card(self):
        return {
            'uuid': self.uuid,
            'title': self.get_formatted_title(),
            'date': self.get_formatted_date(),
            'url': self.url,
            'paragraph': self.description,
            'image': self.get_main_image(),
        }

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['heading_section'] = self.get_heading_section()
        context['journal_section'] = self.get_journal_section()
        return context

    class Meta:
        verbose_name = "Digitized Asset Page"

    def __str__(self):
        return f"Asset: {self.get_formatted_title()}"
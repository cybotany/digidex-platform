import uuid
from django.db import models
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden

from modelcluster.fields import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable

from inventory.forms import DigitalObjectForm, DigitalObjectDeletionForm, DigitalObjectJournalEntryForm


CustomImageModel = get_image_model()

class DigitalObjectPage(RoutablePageMixin, Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        help_text="Digitized Object Name."
    )
    description = RichTextField(
        blank=True,
        null=True,
        help_text="Digitized Object Description."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
    ]

    parent_page_types = [
        'inventory.InventoryCategoryPage',
    ]

    @property
    def collection(self):
        if self.get_collection():
            return self.get_collection()
        return self.create_collection()

    def get_collection(self):
        return self.owner.collection.get_children().filter(name=self.name).first()

    def create_collection(self):
        return self.owner.collection.add_child(name=self.name)

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
        return self.created_at.strftime('%B %d, %Y')
    
    @property
    def formatted_name(self):
        return self.name.title()

    @route(r'^update/$', name='update_digit_view')
    def update_digit_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not authorized to update this digital object.")
        
        if request.method == 'POST':
            form = DigitalObjectForm(request.POST, request.FILES)
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
            form = DigitalObjectForm(initial=initial_data)
        
        return render(request, 'inventory/digit/update.html', {'form': form})

    @route(r'^delete/$', 'delete_digit_view')
    def delete_digit_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not authorized to update this digital object.")

        if request.method == 'POST':
            form = DigitalObjectDeletionForm(request.POST)
            if form.is_valid():
                parent_page = self.get_parent()
                self.delete()
                messages.success(request, 'Digit successfully deleted')
                return redirect(parent_page.url)
        else:
            form = DigitalObjectDeletionForm()
        
        return render(request, 'inventory/digit/delete.html', {'form': form})

    @route(r'^add/$', name='add_digit_entry_view')
    def add_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to update this page.")
        
        if request.method == 'POST':
            form = DigitalObjectJournalEntryForm(request.POST, request.FILES)
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
                journal_entry = DigitalObjectJournalEntry(
                    page=self,
                    image=image,
                    note=note,
                )
                journal_entry.save()
                messages.success(request, 'Journal entry successfully added.')
                return redirect(self.url)
        else:
            form = DigitalObjectJournalEntryForm()
        
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
        return self.name.title()


class DigitalObjectJournalEntry(Orderable):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Journal Entry Collection UUID"
    )
    image = models.ForeignKey(
        CustomImageModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    note = models.TextField(
        blank=True,
        null=True,
        help_text="Journal entry note."
    )
    page = ParentalKey(
        'inventory.DigitalObjectPage',
        on_delete=models.CASCADE,
        related_name='journal_entries',
    )
    entry_number = models.PositiveIntegerField(
        default=1,
        editable=False,
        verbose_name="Journal Entry Number"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y')

    def get_details(self):
        return {
            'image': self.image,
            'date': self.formatted_date,
            'note': self.note,
        }
    
    def save(self, *args, **kwargs):
        if not self.entry_number:
            last_entry = DigitalObjectJournalEntry.objects.filter(page=self.page).order_by('-entry_number').first()
            if last_entry:
                self.entry_number = last_entry.entry_number + 1
            else:
                self.entry_number = 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Journal entry made on {self.created_at}."

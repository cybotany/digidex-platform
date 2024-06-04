import uuid
from django.db import models
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from modelcluster.fields import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable

from inventory.forms import DigitalObjectForm, DigitalObjectDeletionForm, DigitalObjectJournalEntryForm
from .journal import JournalEntry


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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    @route(r'^update/$', name='update_digit_view')
    @login_required
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
    @login_required
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

    @route(r'^add/$', name='add_entry_view')
    @login_required
    def add_view(self, request):
        page_owner = self.user
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")
        
        if request.method == 'POST':
            form = DigitalObjectJournalEntryForm(request.POST)
            if form.is_valid():
                category = apps.get_model('inventory', 'Category')(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description']
                )
                category.save()
                messages.success(request, f'{category.name} successfully added.')
                return redirect(category._page.url)
        else:
            form = DigitalObjectJournalEntryForm()
        
        return render(request, 'inventory/category/add.html', {'form': form})

    def __str__(self):
        return self.name.title()


class DigitalObjectJournalEntry(Orderable, JournalEntry):
    page = ParentalKey(
        'inventory.DigitalObjectPage',
        on_delete=models.CASCADE,
        related_name='journal_entries',
    )

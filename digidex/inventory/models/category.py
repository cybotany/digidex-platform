import uuid
from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from modelcluster.fields import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel

from inventory.forms import InventoryCategoryForm, InventoryCategoryDeletionForm, InventoryCategoryJournalEntryForm

from .journal import JournalEntry


class InventoryCategoryPage(RoutablePageMixin, Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory Category UUID"
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='Category',
        help_text="Inventory Category Name."
    )
    description = RichTextField(
        blank=True,
        null=True,
        help_text="Inventory Category description."
    )
    is_party = models.BooleanField(
        default=False,
        help_text="Indicates if this is the Party category."
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
        'inventory.UserProfilePage'
    ]

    subpage_types = [
        'inventory.InventoryCategoryPage'
    ]

    def get_page_panel_details(self):
        return {
            'name': self.user.username,
            'image': self.image,
            'date': self.created_at, 
            'description': self.introduction,
            'update_url': self.reverse_subpage('update_category_view'),
            'delete_url': self.reverse_subpage('delete_category_view'),
        }

    def get_page_card_details(self):
        return {
        #    'add_url': self.reverse_subpage('add_entry_view'),
            'page_cards': self.get_children()
        }

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    @route(r'^update/$', name='update_category_view')
    @login_required
    def update_view(self, request):
        page_owner = self.user
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = InventoryCategoryForm(request.POST, request.FILES)
            if form.is_valid():
                if 'name' in form.cleaned_data:
                    self.name = form.cleaned_data['name']
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
            form = InventoryCategoryForm(initial=initial_data)

        return render(request, 'inventory/category/update.html', {'form': form, 'url': self.url})

    @route(r'^delete/$', 'delete_category_view')
    @login_required
    def delete_view(self, request):
        page_owner = self.user
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = InventoryCategoryDeletionForm(request.POST)
            if form.is_valid():
                parent_page = self.get_parent()
                self.delete()
                messages.success(request, 'Category successfully deleted')
                return redirect(parent_page.url)
        else:
            form = InventoryCategoryDeletionForm()

        return render(request, 'inventory/category/delete.html', {'form': form, 'url': self.url})

    @route(r'^add/$', name='add_category_entry_view')
    @login_required
    def add_view(self, request):
        page_owner = self.user
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to update this page.")
        
        if request.method == 'POST':
            form = InventoryCategoryJournalEntryForm(request.POST, request.FILES)
            if form.is_valid():
                journal_entry = InventoryCategoryJournalEntryForm(
                    image=form.cleaned_data['image'],
                    caption=form.cleaned_data['caption'],
                    note=form.cleaned_data['note'],
                    page=self
                )
                journal_entry.save()
                messages.success(request, 'Journal entry successfully added.')
                return redirect(self.url)
        else:
            form = InventoryCategoryJournalEntryForm()
        
        return render(request, 'inventory/category/journal.html', {'form': form})


    class Meta:
        verbose_name = "Inventory Category Page"


class InventoryCategoryJournalEntry(Orderable, JournalEntry):
    page = ParentalKey(
        'inventory.InventoryCategoryPage',
        on_delete=models.CASCADE,
        related_name='journal_entries',
    )

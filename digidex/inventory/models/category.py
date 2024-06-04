import uuid
from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from django.utils.text import slugify

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
            'name': self.name,
            'image': None, # self.image,
            'date': self.created_at, 
            'description': self.description,
            'update_url': self.reverse_subpage('update_category_view'),
            'delete_url': self.reverse_subpage('delete_category_view'),
        }

    def get_page_list_details(self):
        return {
            'add_url': self.reverse_subpage('add_category_entry_view'),
            'form_model': 'Journal Entry',
        }

    def get_page_card_details(self):
        return self.get_children()

    @route(r'^update/$', name='update_category_view')
    def update_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = InventoryCategoryForm(request.POST)
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
            form = InventoryCategoryForm(initial=initial_data)

        return render(request, 'inventory/category/update.html', {'form': form, 'url': self.url})

    @route(r'^delete/$', 'delete_category_view')
    def delete_view(self, request):
        page_owner = self.owner
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
    def add_view(self, request):
        page_owner = self.owner
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['page_panel'] = self.get_page_panel_details()
        context['page_tabs'] = self.get_page_list_details()
        context['page_cards'] = self.get_page_card_details()
        return context

    def clean(self):
        super().clean()
        forbidden_keywords = ['add', 'update', 'delete', 'admin']
        if any(keyword in self.name.lower() for keyword in forbidden_keywords):
            raise ValidationError(f'The name cannot contain any of the following keywords: {", ".join(forbidden_keywords)}')

        # Check if the parent already has an object with the same name or slug
        siblings = self.get_siblings(inclusive=False)
        if siblings.filter(title=self.title).exists() or siblings.filter(slug=self.slug).exists():
            raise ValidationError('An inventory category with this name or slug already exists in this parent.')


    class Meta:
        verbose_name = "Inventory Category Page"


class InventoryCategoryJournalEntry(Orderable, JournalEntry):
    page = ParentalKey(
        'inventory.InventoryCategoryPage',
        on_delete=models.CASCADE,
        related_name='journal_entries',
    )

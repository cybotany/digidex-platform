import uuid
from django.db import models
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseForbidden
from django.utils.text import slugify
from django.urls import reverse

from modelcluster.fields import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.api import APIField
from wagtail.images import get_image_model
from wagtail.models import Collection, Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from nfc.models import NearFieldCommunicationLink
from journal.models import Note, NoteImageGallery

from .forms import TrainerForm, DeleteTrainerForm, TrainerInventoryForm, TrainerJournalEntryForm


CustomImageModel = get_image_model()

class TrainerPage(RoutablePageMixin, Page):
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
    introduction = RichTextField(
        null=True,
        blank=True
    )

    api_fields = [
        APIField('uuid'),
        APIField('introduction'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'asset.AssetPage'
    ]

    @property
    def formatted_date(self):
        return self.first_published_at.strftime('%B %d, %Y')
    
    @property
    def formatted_name(self):
        return self.owner.username.title()

    @route(r'^update/$', name='update_profile_view')
    def update_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = TrainerForm(request.POST, request.FILES)
            if form.is_valid():
                if 'image' in form.cleaned_data and form.cleaned_data['image']:
                    image = CustomImageModel(
                        title='User Avatar',
                        file=form.cleaned_data['image'],
                        collection=self.owner.collection
                    )
                    image.save()
                    self.image = image

                if 'introduction' in form.cleaned_data:
                    self.introduction = form.cleaned_data['introduction']
                self.save()
                messages.success(request, 'Profile successfully updated')
                return redirect(self.url)
        else:
            initial_data = {
                'introduction': self.introduction,
                'image': self.image.file if self.image else None,
            }
            form = TrainerForm(initial=initial_data)

        return render(request, 'trainer/includes/update.html', {'form': form, 'url': self.url})

    @route(r'^delete/$', 'delete_profile_view')
    def delete_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = DeleteTrainerForm(request.POST)
            if form.is_valid():
                logout(request)
                page_owner.delete()
                messages.success(request, 'Account successfully deleted')
                return redirect(reverse('home'))
        else:
            form = DeleteTrainerForm()

        return render(request, 'trainer/includes/delete.html', {'form': form, 'url': self.url})

    @route(r'^add/$', name='add_category_view')
    def add_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")
        
        if request.method == 'POST':
            form = TrainerInventoryForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                category_page = apps.get_model('inventory', 'InventoryPage')(
                    title=f"{name.title()}'s Inventory",
                    slug=slugify(name),
                    owner=page_owner,
                    name=name,
                    description=form.cleaned_data['description']
                )
                self.add_child(instance=category_page)
                category_page.save_revision().publish()
                messages.success(request, f'{category_page.name} successfully added!')
                return redirect(category_page.url)
        else:
            form = TrainerInventoryForm()
        
        return render(request, 'trainer/includes/add.html', {'form': form})

    def get_panel(self):
        return {
            'name': self.formatted_name,
            'image': self.image,
            'date': self.formatted_date, 
            'description': self.introduction or 'No description available',
            'update_url': self.reverse_subpage('update_profile_view'),
            'delete_url': self.reverse_subpage('delete_profile_view'),
        }

    def get_inventory_collection(self):
        _categorytype = ContentType.objects.get(app_label='inventory', model='InventoryPage')
        return self.get_children().filter(content_type=_categorytype)

    def get_inventory(self, name=None):
        _collection = self.get_inventory_collection()
        if name:
            try:
                inventory = _collection.get(slug=name)
            except Page.DoesNotExist:
                pass            
        else:
            inventory = _collection.get(slug='party')
        return inventory

    def get_asset_collection(self, inventory):
        _type = ContentType.objects.get(app_label='inventory', model='AssetPage')
        _collection = inventory.get_children().filter(content_type=_type)
        _assets = [_asset.specific.get_card_details() for _asset in _collection]
        return _assets

    def get_category_section(self):
        return {
            'name': self.formatted_name,
            'image': self.image,
            'date': self.formatted_date, 
            'description': self.introduction or 'No description available',
            'update_url': self.reverse_subpage('update_profile_view'),
            'delete_url': self.reverse_subpage('delete_profile_view'),
        }

    def get_featured_asset(self):
        return {
            'name': self.formatted_name,
            'image': self.image,
            'date': self.formatted_date, 
            'description': self.introduction or 'No description available',
            'update_url': self.reverse_subpage('update_profile_view'),
            'delete_url': self.reverse_subpage('delete_profile_view'),
        }

    def get_asset_collection(self):
        return {
            'name': self.formatted_name,
            'image': self.image,
            'date': self.formatted_date, 
            'description': self.introduction or 'No description available',
            'update_url': self.reverse_subpage('update_profile_view'),
            'delete_url': self.reverse_subpage('delete_profile_view'),
        }

    def get_inventory(self, tab_name=None):
        from django.contrib.contenttypes.models import ContentType
        _categorytype = ContentType.objects.get(app_label='inventory', model='InventoryPage')
        _categories = self.get_children().filter(content_type=_categorytype)

        if tab_name:
            try:
                tab = _categories.get(slug=tab_name)
            except Page.DoesNotExist:
                pass            
        else:
            tab = _categories.get(slug='party')
        
        categories = _categories.exclude(id=tab.id)
        category_list = [category.specific.get_card_details() for category in categories]

        _cardtype = ContentType.objects.get(app_label='inventory', model='AssetPage')
        _cards = tab.get_children().filter(content_type=_cardtype)
        
        card_list = [_card.specific.get_card_details() for _card in _cards]
     
        return {
            'tab': tab.specific,
            'cards': card_list,
            'categories': category_list,
            'add_url': self.reverse_subpage('add_category_view'),
            'form_model': 'Category',
        }

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['featured_asset'] = self.get_panel()
        context['category_collection'] = self.get_inventory()
        context['asset_collection'] = self.get_inventory()
        return context

    class Meta:
        verbose_name = "User Profile Page"


class TrainerNote(Note):
    trainer = models.ForeignKey(
        TrainerPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Trainer Note: {self.uuid}"


class TrainerNoteImageGallery(NoteImageGallery):
    note = ParentalKey(
        TrainerNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    panels = NoteImageGallery.panels +  [
        InlinePanel('gallery_images', label="Note Image Gallery"),
    ]


class TrainerNearFieldCommunicationLink(NearFieldCommunicationLink):
    trainer = models.OneToOneField(
        TrainerPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    def __str__(self):
        return f"Trainer NFC: {self.uuid}"

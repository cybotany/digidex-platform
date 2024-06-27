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

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.api import APIField
from wagtail.images import get_image_model
from wagtail.models import Collection, Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.users.models import UserProfile

from .forms import TrainerForm, DeleteTrainerForm, TrainerInventoryForm


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
        'inventory.InventoryPage'
    ]

    def get_user_profile(self):
        return UserProfile.objects.get(user=self.owner)

    @property
    def formatted_date(self):
        if self.live:
            return self.first_published_at.strftime('%B %d, %Y')
        return "Draft"
    
    @property
    def formatted_title(self):
        return self.owner.username.title()

    @route(r'^update/$', name='update_trainer_view')
    def update_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = TrainerForm(request.POST, request.FILES)
            if form.is_valid():
                if 'introduction' in form.cleaned_data:
                    self.introduction = form.cleaned_data['introduction']
                self.save()
                messages.success(request, 'Profile successfully updated')
                return redirect(self.url)
        else:
            initial_data = {
                'introduction': self.introduction,
            }
            form = TrainerForm(initial=initial_data)

        return render(request, 'trainer/includes/update_form.html', {'form': form})

    @route(r'^delete/$', 'delete_trainer_view')
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

        return render(request, 'trainer/includes/delete_form.html', {'form': form})

    @route(r'^add/$', name='add_inventory_view')
    def add_view(self, request):
        page_owner = self.owner
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")
        
        if request.method == 'POST':
            form = TrainerInventoryForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                inventory_page = apps.get_model('inventory', 'inventorypage')(
                    title=title.title(),
                    slug=slugify(title),
                    owner=page_owner,
                    description=form.cleaned_data['description']
                )
                self.add_child(instance=inventory_page)
                inventory_page.save_revision().publish()
                messages.success(request, f'{title} successfully added!')
                return redirect(inventory_page.url)
        else:
            form = TrainerInventoryForm()
        
        return render(request, 'trainer/includes/inventory_form.html', {'form': form})

    def get_page_heading(self):
        return {
            'title': f"Trainer {self.formatted_title}",
            'paragraph': self.introduction,
            'update_url': self.reverse_subpage('update_trainer_view'),
            'delete_url': self.reverse_subpage('delete_trainer_view'),
        }

    def get_inventory_collection(self):
        _categorytype = ContentType.objects.get(app_label='inventory', model='inventorypage')
        return self.get_children().filter(content_type=_categorytype)

    def get_asset_collection(self, inventory):
        _type = ContentType.objects.get(app_label='asset', model='assetpage')
        _collection = inventory.get_children().filter(content_type=_type)
        _assets = [_asset.specific.get_summary() for _asset in _collection]
        return _assets

    def get_context(self, request, *args, **kwargs):
        category_collection = list(self.get_inventory_collection())
        default_category = category_collection.pop(0) if category_collection else None
        category_section = {
            'title': 'Inventory',
            'collection': category_collection,
            'default': default_category,
            'add_url': self.reverse_subpage('add_inventory_view'),
        }

        asset_collection = self.get_asset_collection(default_category)
        default_asset = asset_collection[0]
        asset_section = {
            'title': 'Assets',
            'collection': asset_collection,
            'default': default_asset,
        }
        
        context = super().get_context(request, *args, **kwargs)
        context['page_heading'] = self.get_page_heading()
        context['category_section'] = category_section
        context['asset_section'] = asset_section
        return context

    class Meta:
        verbose_name = "User Trainer Page"

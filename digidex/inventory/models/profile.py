import uuid
from django.db import models
from django.apps import apps
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from base.utils.storage import PublicMediaStorage
from inventory.forms import UserProfileForm, InventoryCategoryForm, DeleteUserForm


def user_avatar_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'users/{instance.uuid}/avatar.{extension}'


class UserProfileIndexPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    introduction = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('introduction'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'inventory.UserProfilePage'
    ]


class UserProfilePage(RoutablePageMixin, Page):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        db_index=True,
        null=True,
        related_name='profile',
        verbose_name="User Profile User"
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User Profile UUID"
    )
    image = models.ImageField(
        storage=PublicMediaStorage(),
        upload_to=user_avatar_path,
        null=True,
        blank=True,
        verbose_name="User Profile Avatar"
    )
    heading = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="User Profile Heading"
    )
    introduction = models.TextField(
        null=True,
        blank=True,
        help_text="Short Biography about the user."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified"
    )

    parent_page_types = [
        'inventory.UserProfileIndexPage'
    ]

    subpage_types = [
        'inventory.InventoryCategoryPage'
    ]

    def get_upload_to_base_path(self):
        return f'users/{self.uuid}'

    def get_upload_to(self, subdirectory, filename):
        extension = filename.split('.')[-1]
        return f'{self.get_upload_to_base_path()}/{subdirectory}/{uuid.uuid4()}.{extension}'

    def get_inventory_categories(self):
        return self.inventory_categories.select_related('detail_page').all()

    def get_page_panel_details(self):
        return {
            'name': self.user.username,
            'date': self.created_at, 
            'description': self.introduction,
            'update_url': self.reverse_subpage('update_profile_view'),
            'delete_url': self.reverse_subpage('delete_profile_view'),
        }

    def get_page_card_details(self):
        return {
            'add_url': self.reverse_subpage('add_category_view'),
            'page_cards': self.get_inventory_categories()
        }

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['page_panel'] = self.get_page_panel_details
        context['page_cards'] = self.get_page_card_details()
        return context

    @route(r'^update/$', name='update_profile_view')
    @login_required
    def update_view(self, request):
        page_owner = self.user
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                if 'image' in form.cleaned_data:
                    self.image = form.cleaned_data['image']
                if 'bio' in form.cleaned_data:
                    self.introduction = form.cleaned_data['bio']
                self.save()
                messages.success(request, 'Profile successfully updated')
                return redirect(self.url)
        else:
            initial_data = {
                'bio': self.introduction,
                'image': self.image
            }
            form = UserProfileForm(initial=initial_data)

        return render(request, 'inventory/profile/update.html', {'form': form, 'url': self.url})

    @route(r'^delete/$', 'delete_profile_view')
    @login_required
    def delete_view(self, request):
        page_owner = self.user
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")

        if request.method == 'POST':
            form = DeleteUserForm(request.POST)
            if form.is_valid():
                logout(request)
                page_owner.delete()
                messages.success(request, 'Account successfully deleted')
                return redirect(reverse('home'))
        else:
            form = DeleteUserForm()

        return render(request, 'inventory/profile/delete.html', {'form': form, 'url': self.url})

    @route(r'^add/$', name='add_category_view')
    @login_required
    def add_view(self, request):
        page_owner = self.user
        if page_owner != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")
        
        if request.method == 'POST':
            form = InventoryCategoryForm(request.POST)
            if form.is_valid():
                category = apps.get_model('inventory', 'Category')(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description']
                )
                category.save()
                messages.success(request, f'{category.name} successfully added.')
                return redirect(category._page.url)
        else:
            form = InventoryCategoryForm()
        
        return render(request, 'inventory/category/add.html', {'form': form})

    class Meta:
        verbose_name = "User Profile Page"

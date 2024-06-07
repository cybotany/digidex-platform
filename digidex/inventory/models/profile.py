import uuid
from django.db import models
from django.apps import apps
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils.text import slugify
from django.urls import reverse

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.models import Page
from wagtail.images import get_image_model
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from inventory.forms import UserProfileForm, InventoryCategoryForm, DeleteUserForm


CustomImageModel = get_image_model()

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
    image = models.ForeignKey(
        CustomImageModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    introduction = RichTextField(
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

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('introduction'),
    ]

    parent_page_types = [
        'inventory.UserProfileIndexPage'
    ]

    subpage_types = [
        'inventory.InventoryCategoryPage'
    ]

    @property
    def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y')
    
    @property
    def formatted_name(self):
        return self.user.username.title()

    def get_page_panel_details(self):
        return {
            'name': self.formatted_name,
            'image': self.image,
            'date': self.formatted_date, 
            'description': self.introduction,
            'update_url': self.reverse_subpage('update_profile_view'),
            'delete_url': self.reverse_subpage('delete_profile_view'),
        }

    def get_page_tab_details(self):
        return {
            'descendants': self.get_children(),
            'add_url': self.reverse_subpage('add_category_view'),
            'form_model': 'Category',
        }

    def get_page_card_details(self):
        return self.get_first_child().get_children()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['page_panel'] = self.get_page_panel_details()
        context['page_tabs'] = self.get_page_tab_details()
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
                if 'image' in form.cleaned_data and form.cleaned_data['image']:
                    image = CustomImageModel(
                        title='User Avatar',
                        file=form.cleaned_data['image'],
                        collection=self.user.collection
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
                name = form.cleaned_data['name']
                category_page = apps.get_model('inventory', 'InventoryCategoryPage')(
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
            form = InventoryCategoryForm()
        
        return render(request, 'inventory/category/add.html', {'form': form})

    class Meta:
        verbose_name = "User Profile Page"

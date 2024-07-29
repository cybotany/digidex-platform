from django.db import models
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404

from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.models import Page, Collection, Site
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

from inventory.models import UserInventory, InventoryCategory, InventoryAsset
from inventory.forms import UserInventoryForm, InventoryCategoryForm, InventoryAssetForm, DeletionConfirmationForm


class HomePage(RoutablePageMixin, Page):
    parent_page_types = [
        'wagtailcore.Page'
    ]

    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    body = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("body")
    )

    content_panels = Page.content_panels + [
        FieldPanel('collection'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title

    @path('<slug:inventory_slug>/')
    def user_inventory(self, request, inventory_slug):
        inventory = get_object_or_404(UserInventory, slug=inventory_slug)		
        return self.render(
            request,
            template='inventory/index/index_page.html',
            context_overrides=inventory.get_template_context_data()
        )

    @path('<slug:inventory_slug>/delete/')
    def delete_user_inventory(self, request, inventory_slug):
        inventory = get_object_or_404(UserInventory, slug=inventory_slug)
        if request.user != inventory.owner:
            raise PermissionDenied

        if request.method == "POST":
            form = DeletionConfirmationForm(request.POST)
            if form.is_valid():
                inventory.delete()
                site = Site.find_for_request(request)
                if site is not None:
                    home_page_url = site.root_page.url
                else:
                    home_page_url = reverse('/')
                return HttpResponseRedirect(home_page_url)
        else:
            form = DeletionConfirmationForm()

        return self.render(
            request,
            template='inventory/forms/delete_index.html',
            context_overrides={'form': form}
        )

    @path('<slug:inventory_slug>/update/')
    def update_user_inventory(self, request, inventory_slug):
        inventory = get_object_or_404(UserInventory, slug=inventory_slug)
        if request.user != inventory.owner:
            raise PermissionDenied

        if request.method == "POST":
            form = UserInventoryForm(request.POST, instance=inventory)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(inventory.get_url())
        else:
            form = UserInventoryForm(instance=inventory)
        
        return self.render(
            request,
            template='inventory/forms/update_index.html',
            context_overrides={'form': form}
        )

    @path('<slug:inventory_slug>/add-category/')
    def add_inventory_category(self, request, inventory_slug):
        inventory = get_object_or_404(UserInventory, slug=inventory_slug)
        if request.user != inventory.owner:
            raise PermissionDenied

        if request.method == "POST":
            form = InventoryCategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.inventory = inventory
                category.save()
                return HttpResponseRedirect(inventory.get_url())
        else:
            form = InventoryCategoryForm()
        
        return self.render(
            request,
            template='inventory/forms/add_category.html',
            context_overrides={'form': form}
        )

    @path('<slug:inventory_slug>/add-asset/')
    def add_inventory_asset(self, request, inventory_slug):
        inventory = get_object_or_404(UserInventory, slug=inventory_slug)
        if request.user != inventory.owner:
            raise PermissionDenied

        if request.method == "POST":
            form = InventoryAssetForm(request.POST)
            if form.is_valid():
                asset = form.save(commit=False)
                asset.inventory = inventory
                asset.save()
                return HttpResponseRedirect(inventory.get_url())
        else:
            form = InventoryAssetForm()
        
        return self.render(
            request,
            template='inventory/forms/add_asset.html',
            context_overrides={'form': form}
        )

    @path('<slug:inventory_slug>/<slug:child_slug>/')
    def inventory_child(self, request, inventory_slug, child_slug):
        inventory = get_object_or_404(UserInventory, slug=inventory_slug)
        try:
            child = inventory.get_category(child_slug)
            template = 'inventory/category/category_page.html'
        except InventoryCategory.DoesNotExist:
            try:
                child = inventory.get_asset(child_slug)
                template = 'inventory/asset/asset_page.html'
            except InventoryAsset.DoesNotExist:
                raise Http404
        return self.render(
            request,
            template=template,
            context_overrides=child.get_template_context_data()
        )

    class Meta:
        verbose_name = _('homepage')

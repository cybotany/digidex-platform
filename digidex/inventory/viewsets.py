from django.shortcuts import render
from django.urls import path

from wagtail.admin.viewsets.base import ViewSet, ViewSetGroup

from .models import Inventory, InventoryCategory, InventoryItem


def index(request):
    user_inventory = Inventory.objects.filter(owner=request.user)
    children = user_inventory.get_children()
    return render(request, 'inventory/index.html', {
        'inventory': user_inventory,
        'children': children,
    })

def catagory_detail(request, catagory_slug):
    user_inventory = Inventory.objects.filter(owner=request.user)
    catagories = InventoryCategory.objects.filter(owner=request.user)
    items = InventoryItem.objects.filter(owner=request.user)
    return render(request, 'inventory/catagory_detail.html', {
        'inventory': user_inventory,
        'catagories': catagories,
        'items': items,
    })


class CatagoryViewSet(ViewSet):
    add_to_admin_menu = False
    menu_label = "Catagories"
    icon = "date"
    # The `name` will be used for both the URL prefix and the URL namespace.
    # They can be customised individually via `url_prefix` and `url_namespace`.
    name = "catagory"

    def get_urlpatterns(self):
        return [
            # This can be accessed at `/admin/calendar/`
            # and reverse-resolved with the name `calendar:index`.
            # This first URL will be used for the menu item, but it can be
            # customized by overriding the `menu_url` property.
            path('', index, name='index'),

            # This can be accessed at `/admin/calendar/month/`
            # and reverse-resolved with the name `calendar:month`.
            path('month/', month, name='month'),
        ]


def catagory_list(request):
    catagories = InventoryCategory.objects.all()
    return render(request, 'wagtailcalendar/event_list.html', {
        'catagories': catagories,
    })

def catagory_detail(request, catagory_id):
    catagory = InventoryCategory.objects.get(id=catagory_id)
    return render(request, 'wagtailcalendar/event_detail.html', {
        'catagory': catagory,
    })


class ItemViewSet(ViewSet):
    add_to_admin_menu = False
    menu_label = "Items"
    icon = "user"
    name = "items"

    def item_detail(request, item_slug):
        user_inventory = Inventory.objects.filter(owner=request.user)
        catagories = InventoryCategory.objects.filter(owner=request.user)
        items = InventoryItem.objects.filter(owner=request.user)
        return render(request, 'inventory/item_detail.html', {
            'inventory': user_inventory,
            'catagories': catagories,
            'items': items,
        })

    def get_urlpatterns(self):
        return [
            path('', item_list, name='item-list'),
            path('<int:item_id>/', item_detail, name='item-detail'),
        ]
    


class InventoryViewSetGroup(ViewSetGroup):
    add_to_admin_menu = True
    menu_label = "Inventory"
    menu_icon = "desktop"
    # You can specify instances or subclasses of `ViewSet` in `items`.
    items = (CatagoryViewSet(), ItemViewSet)

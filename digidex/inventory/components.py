from django.urls import reverse

from laces.components import Component

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    TextComponent,
    CollectionComponent,
    EmptyComponent,
    ButtonComponent,
)
from inventory.models import InventoryIndex


class ItemComponent(Component):
    template_name = 'inventory/components/item.html'

    def __init__(self, item=dict(), style=None):
        self.item = item
        self.style = self.set_style(style)

    def set_style(self, style):
        if style:
            return style
        return 'post'

    def get_heading_component(self):
        return HeadingComponent(
            text=self.item.get('heading', 'No heading available'),
            size=4,
            style=self.style
        )

    def get_paragraph_component(self):
        return ParagraphComponent(
            text=self.item.get('paragraph', 'No paragraph available'),
            style=self.style
        )

    def get_context_data(self, parent_context=None):
        return {
            "date": self.item.get('date', ''),
            "url": self.item.get('url', ''),
            "heading": self.get_heading_component(),
            "paragraph": self.get_paragraph_component(),
            "thumbnail": self.item.get('thumbnail', '')
        }


class ItemCollectionPanel(Component):
    template_name = 'inventory/panels/items.html'

    def __init__(self, items):
        self.items = items
        self.children = [ItemComponent(item) for item in items]

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children
        }


class CategoryComponent(Component):
    template_name = 'inventory/components/category.html'

    def __init__(self, category=dict()):
        self.category = category

    def get_context_data(self, parent_context=None):
        return {
            "url": self.category.get('url', ''),
            "text": self.category.get('text', ''),
        }


class CategoryCollectionPanel(Component):
    template_name = 'inventory/panels/categories.html'

    def __init__(self, categories):
        self.categories = categories
        self.children = [CategoryComponent(category) for category in categories]

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children
        }


class DashboardComponent(Component):
    template_name = 'inventory/panels/dashboard.html'

    def __init__(self, user):
        self.user = user
        self.inventory = InventoryIndex.objects.get(owner=user)
        self.categories = self.inventory.get_categories()
        self.party = self.inventory.get_party()
        self.items = self.inventory.get_items()
        self.panels = [
            self.get_body_panel(),
        ]

    def get_context_data(self, parent_context=None):
        return {
            "panels": self.panels
        }

    def get_body_panel(self):
        items = self.items
        children = []
        count_of_items = len(items)

        if  count_of_items >= 1:
            featured_item = items.pop(0)
            featured_panel = self._get_featured_item_panel(featured_item)
            children.append(featured_panel)

            # Check if there are any items left
            if items:
                items_panel = self._get_items_panel(items)
                children.append(items_panel)

        else:
            empty_component = self._get_empty_panel(assets="items")
            children.append(empty_component)

        panel = SectionComponent(
            children=children
        )
        return panel


    def _get_featured_item_panel(self, featured_item):
        return FeaturedItemComponent(featured_item)


    def _get_items_panel(self, items):
        style = 'posts'
        item_components = [ItemComponent(item) for item in items]
        panel = CollectionComponent(
            children=item_components,
            style=style
        )
        return panel

    def _get_empty_panel(self, asset):
        return EmptyComponent(asset=asset)

from django.urls import reverse

from laces.components import Component

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    IconComponent,
    TextComponent,
    CollectionComponent,
    EmptyComponent,
    ButtonComponent,
)


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


class ItemCollectionComponent(Component):
    template_name = 'inventory/components/item_collection.html'

    def __init__(self, items):
        self.items = items

    def get_featured_item_collection(self, featured_item):
        style = 'post large'
        return CollectionComponent(
            children=[ItemComponent(featured_item, style=style)],
            style=style,
        )

    def get_item_collection(self):
        style = 'post'
        return CollectionComponent(
            children=[ItemComponent(item, style) for item in self.items],
            style=style,
        )

    def set_panel(self):
        panel_components = []

        if self.items:
            featured_item = self.items.pop(0)
            panel_components.append(self.get_featured_item_collection(featured_item))

            if self.items: # Check if there are any items left
                panel_components.append(self.get_item_collection())

        else:
            panel_components.append(EmptyComponent(assets="items"))

        return SectionComponent(children=panel_components)

    def get_context_data(self, parent_context=None):
        return {
            "panel": self.set_panel()
        }


class CategoryComponent(Component):
    template_name = 'inventory/components/category.html'

    def __init__(self, category=dict(), current=False):
        self.category = category
        self.current = current
        self.style = 'category'

    def get_icon_component(self):
        return IconComponent(
            source=self.category.get('icon_source', ''),
            alt=self.category.get('alt_text', ''),
            style=self.style
        )

    def get_text_component(self):
        return TextComponent(
            text=self.category.get('text', 'No text available'),
            style=self.style
        )

    def get_context_data(self, parent_context=None):
        return {
            "url": self.category.get('url', ''),
            "icon": self.get_icon_component(),
            "text": self.get_text_component()
        }


class CategoryCollectionComponent(Component):
    template_name = 'inventory/components/category_collection.html'

    def __init__(self, categories):
        self.categories = categories

    def get_current_category(self, current_category):
        return CategoryComponent(current_category, current=True)

    def get_category_collection(self):
        style = 'categories'
        return CollectionComponent(
            children=[CategoryComponent(category) for category in self.categories],
            style=style
        )

    def set_panel(self):
        panel_components = []

        if self.categories:
            current_category = self.categories.pop(0)
            panel_components.append(self.get_current_category(current_category))

            if self.categories: # Check if there are any categories left
                panel_components.append(self.get_category_collection())

        else:
            panel_components.append(EmptyComponent(assets="categories"))

        return SectionComponent(children=panel_components)

    def get_context_data(self, parent_context=None):
        return {
            "children": self.set_panel
        }

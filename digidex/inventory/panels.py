from base.components import (
    Component,
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
    DateComponent,
)


class InventoryCategoryPanel(Component):
    template_name = 'inventory/panels/category_panel.html'

    def __init__(self, category):
        self.category = category.get_panel_data()

    def get_context_data(self, parent_context=None):
        return {
            "name": self.category.get('name', 'No name available'),
            "url": self.category.get('url', '#'),
            "thumbnail": self.category.get('thumbnail', None)
        }


class InventoryCategoryCollection(Component):
    template_name = 'inventory/components/category_collection.html'

    def __init__(self, categories=list()):
        self.categories = categories

    def get_category_collection(self):
        style = 'categories'
        return CollectionComponent(
            children=[category.get_component() for category in self.categories],
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
            panel_components.append(EmptyComponent(asset="categories"))

        return BlockComponent(children=panel_components)

    def get_context_data(self, parent_context=None):
        return {
            "panel": self.set_panel()
        }


class InventoryHeaderPanel(Component):
    template_name = "inventory/panels/header.html"

    def __init__(self, inventory):
        self.inventory = inventory
        self.style = "top"

    def get_heading(self):
        return HeadingComponent(
            text=self.inventory.title,
            size=1,
            style=self.style
        )

    def _get_collection(self, categories):
        collection = []
        for category in categories:
            collection.append(InventoryCategoryPanel(category=category))
        return collection

    def get_categories(self):
        STYLE = 'categories'
        categories = self.inventory.get_categories()
        if categories:
            collection = self._get_collection(categories)
            return CollectionComponent(
                children=collection,
                style=STYLE
            )
        return EmptyComponent(type=STYLE) 

    def get_context_data(self, parent_context=None):
        return {
            "heading": self.get_heading(),
            "categories": self.get_categories()
        }


class AssetPanel(Component):
    template_name = 'inventory/panels/asset_panel.html'

    def __init__(self, asset=dict()):
        self.heading = asset.get('heading', 'No heading available')
        self.paragraph = asset.get('paragraph', 'No paragraph available')
        self.date = asset.get('date')
        self.url = asset.get('url')
        self.thumbnail = asset.get('thumbnail')
        self.style = 'post'

    def get_heading_component(self):
        return HeadingComponent(
            text=self.heading,
            size=4,
            style=self.style
        )

    def get_paragraph_component(self):
        return ParagraphComponent(
            text=self.paragraph,
            style=self.style
        )

    def get_date_component(self):
        return DateComponent(
            date=self.date
        )

    def get_context_data(self, parent_context=None):
        return {
            "date": self.get_date_component(),
            "url": self.url,
            "heading": self.get_heading_component(),
            "paragraph": self.get_paragraph_component(),
            "thumbnail": self.thumbnail
        }

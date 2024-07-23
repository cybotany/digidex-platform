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
    DateComponent,
)


class CategoryPanel(Component):
    template_name = 'inventory/panels/category_panel.html'

    def __init__(self, category=dict(), current=False):
        self.url = category.get('url')
        self.icon_source = category.get('icon_source')
        self.icon_alt = category.get('icon_alt')
        self.name = category.get('name', 'No name available')
        self.current = current
        self.style = 'category'

    def get_icon_component(self):
        return IconComponent(
            source=self.icon_source,
            alt=self.icon_alt,
            style=self.style
        )

    def get_text_component(self):
        return TextComponent(
            text=self.name,
            style=self.style
        )

    def get_context_data(self, parent_context=None):
        return {
            "url": self.url,
            "icon": self.get_icon_component() if self.icon_source else None,
            "text": self.get_text_component(),
            "current": self.current
        }


class CategoryCollection(Component):
    template_name = 'inventory/components/category_collection.html'

    def __init__(self, categories=list()):
        self.categories = categories

    def get_current_category(self, current_category):
        return current_category.get_component(current=True)

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

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


class CategoryComponent(Component):
    template_name = 'category/components/category.html'

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


class CategoryCollectionComponent(Component):
    template_name = 'category/components/category_collection.html'

    def __init__(self, categories):
        self.categories = list(categories)

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
            "panel": self.set_panel
        }

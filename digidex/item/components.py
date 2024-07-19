from django.forms import Media

from laces.components import Component, MediaContainer

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

class ItemCard(Component):
    template_name = 'item/components/item_card.html'

    def __init__(self, item=dict(), featured=None):
        self.heading = self.item.get('heading', 'No heading available')
        self.paragraph = self.item.get('paragraph', 'No paragraph available')
        self.date = self.item.get('date')
        self.url = self.item.get('url')
        self.thumbnail = self.item.get('thumbnail')
        self.style = self.get_style(featured)

    def get_style(self, featured):
        if featured:
            return 'post large'
        return 'post'

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


class ItemCollection(Component):
    template_name = 'item/components/item_collection.html'

    def __init__(self, items):
        self.items = items

    @property
    def media(self):
        return Media(
            css={"all": ("item/css/item_collection.css",)}
        )

    def get_featured_item_collection(self, featured_item):
        style = 'post large'
        return CollectionComponent(
            children=[featured_item.get_component(featured=True)],
            style=style,
        )

    def get_item_collection(self):
        style = 'post'
        return CollectionComponent(
            children=[item.get_component() for item in self.items],
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
            panel_components.append(EmptyComponent(asset="items"))

        return SectionComponent(children=panel_components)

    def get_context_data(self, parent_context=None):
        return {
            "panel": self.set_panel()
        }

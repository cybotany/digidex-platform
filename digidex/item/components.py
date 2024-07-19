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

class ItemPanel(Component):
    template_name = 'item/components/item_panel.html'

    def __init__(self, item=dict()):
        self.heading = self.item.get('heading', 'No heading available')
        self.paragraph = self.item.get('paragraph', 'No paragraph available')
        self.date = self.item.get('date')
        self.url = self.item.get('url')
        self.thumbnail = self.item.get('thumbnail')
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

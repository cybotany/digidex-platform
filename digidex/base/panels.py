from django.forms import Media

from laces.components import Component

from .components import (
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


class HeaderComponent(Component):
    template_name = 'base/header.html'

    def __init__(self, header=dict()):
        self.heading = header.get('heading', 'No heading available')
        self.paragraph = header.get('paragraph')
        self.categories = header.get('categories')
        self.style = 'top'

    @property
    def media(self):
        return Media(
            css={"all": ("base/css/header.css",)}
        )

    def get_heading_component(self):
        return HeadingComponent(
            text=self.heading,
            size=1,
            style=self.style
        )

    def get_paragraph_component(self):
        return ParagraphComponent(
            text=self.paragraph,
            style=self.style
        )

    def get_block_component(self):
        block_children = [
            self.get_heading_component(),
        ]

        if self.paragraph:
            block_children.append(self.get_paragraph_component())

        if self.categories:
            block_children.append(self.categories)

        return BlockComponent(
            children=block_children,
            style=self.style
        )

    def set_top_panel(self):
        return SectionComponent(
            children=[self.get_block_component()],
            style=self.style
        )

    def get_context_data(self, parent_context=None):
        return {
            "panel": self.set_top_panel()
        }

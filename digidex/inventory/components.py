from laces.components import Component

from base.components import HeadingComponent, ParagraphComponent


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


class CategoryComponent(Component):
    template_name = 'inventory/components/category.html'

    def __init__(self, category=dict()):
        self.category = category

    def get_context_data(self, parent_context=None):
        return {
            "url": self.category.get('url', ''),
            "text": self.category.get('text', ''),
        }

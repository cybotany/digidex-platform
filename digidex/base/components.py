from laces.components import Component


class SectionComponent(Component):
    template_name = "base/components/section.html"

    def __init__(self, children=list[Component], style=str):
        self.children = children
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children,
            "style": self.style
        }


class BlockComponent(Component):
    template_name = 'base/components/block.html'

    def __init__(self, children=list[Component], style=str):
        self.children = children
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children,
            "style": self.style
        }


class HeadingComponent(Component):
    template_name = 'base/components/heading.html'

    def __init__(self, text=str, size=int, style=str):
        self.text = text
        self.size = size
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "size": self.size,
            "style": self.style
        }


class ParagraphComponent(Component):
    template_name = 'base/components/paragraph.html'

    def __init__(self, text=str, style=str):
        self.text = text
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "style": self.style
        }


class LinkComponent(Component):
    template_name = 'base/components/link.html'

    def __init__(self, url=str, text=str, style=str):
        self.url = url
        self.text = text
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "url": self.url,
            "text": self.text,
            "style": self.style
        }


class IconComponent(Component):
    template_name = 'base/components/icon.html'

    def __init__(self, source=None, alt = None, style=None):
        self.source = source
        self.alt = alt
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "source": self.source,
            "alt": self.alt,
            "style": self.style
        }


class ImageComponent(Component):
    template_name = 'base/components/image.html'

    def __init__(self, source=str, alt=None, style=None):
        self.source = source
        self.alt = alt
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "source": self.source,
            "style": self.style
        }


class TextComponent(Component):
    template_name = 'base/components/text.html'

    def __init__(self, text=str, style=str):
        self.text = text
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "style": self.style
        }


class CollectionComponent(Component):
    template_name = 'base/components/collection.html'

    def __init__(self, children=list[Component], style=str):
        self.children = children
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children,
            "style": self.style
        }


class EmptyComponent(Component):
    template_name = 'base/components/empty.html'

    def __init__(self, asset=str):
        self.asset = asset

    def get_context_data(self, parent_context=None):
        return {
            "asset": self.asset
        }


class ButtonComponent(Component):
    template_name = 'base/components/button.html'

    def __init__(self, url=str, text=str, style=str):
        self.url = url
        self.text = text
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "url": self.url,
            "text": self.text,
            "style": self.style
        }


class DateComponent(Component):
    template_name = 'base/components/date.html'

    def __init__(self, date=str, style=None):
        self.date = date
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "date": self.date,
            "style": self.style
        }

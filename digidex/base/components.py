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


class LinkWrapperComponent(Component):
    template_name = 'base/components/link_wrapper.html'

    def __init__(self, url=str, children=list[Component], style=str):
        self.url = url
        self.children = children
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "url": self.url,
            "children": self.children,
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

    def __init__(self, source=str, alt=str, style=str):
        self.source = source
        self.alt = alt
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "source": self.source,
            "alt": self.alt,
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


class NavigationComponent(Component):
    template_name = 'base/components/navigation.html'

    def __init__(self, links=list[Component], buttons=list[Component]):
        self.links = links
        self.buttons = buttons

    def get_context_data(self, parent_context=None):
        return {
            "links": self.links,
            "buttons": self.buttons
        }

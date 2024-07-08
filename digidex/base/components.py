from dataclasses import dataclass, asdict

from laces.components import Component


@dataclass
class Section(Component):
    template_name = "base/components/section.html"

    style: str = 'section'
    children: list[Component]

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class Block(Component):
    template_name = 'base/components/block.html'

    style: str = 'block'
    children: list[Component]

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class Heading(Component):
    template_name = 'base/components/heading.html'

    style: str = 'heading'
    text: str
    size: int = 2

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class Paragraph(Component):
    template_name = 'base/components/paragraph.html'

    style: str = 'paragraph'
    text: str

    def get_context_data(self, parent_context=None):
        return asdict(self)

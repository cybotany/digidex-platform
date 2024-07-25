from base.components import (
    Component,
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    IconComponent,
    ImageComponent,
    TextComponent,
    CollectionComponent,
    EmptyComponent,
    ButtonComponent,
    DateComponent
)


class PageHeaderPanel(Component):
    template_name = "base/panels/header.html"

    def __init__(self, page):
        self.page = page
        self.style = "top"

    def get_heading(self):
        return HeadingComponent(
            text=self.page.title,
            size=1,
            style=self.style
        )

    def get_paragraph(self):
        return ParagraphComponent(
            text=self.page.search_description,
            line_break=False,
            style=self.style
        )

    def get_categories(self):
        pass

    def get_children(self):
        children = [
            self.get_heading()
        ]
        if self.page.search_description:
            children.append(self.get_paragraph())
        return children
    

    def get_context_data(self, parent_context=None):
        return {"children": self.get_children()}

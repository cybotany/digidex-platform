from wagtail.blocks import StructBlock, CharBlock, URLBlock, ListBlock, StreamBlock


class TextLink(StructBlock):
    url = URLBlock(
        required=True,
        help_text="Enter the URL to link to"
    )
    text = CharBlock(
        required=True,
        help_text="Enter the text to display"
    )

    class Meta:
        icon = "link"
        label = "Link"


class Heading(StructBlock):
    text = CharBlock(
        required=True
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading.html"


class Subtitle(StructBlock):
    subtitle = CharBlock(
        required=True
    )

    class Meta:
        template = "base/blocks/subtitle.html"


class HeadingBlock(StructBlock):
    subtitle = CharBlock(
        classname="title",
        required=False
    )
    title = CharBlock(
        classname="title",
        required=True
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading.html"


class FootnoteBlock(StructBlock):
    text = CharBlock(
        required=False
    )
    link = TextLink(
        required=True
    )

    class Meta:
        template = "base/blocks/footnote.html"


class LeftBlock(StreamBlock):

    class Meta:
        template = "base/blocks/grid.html"


class RightBlock(StreamBlock):

    class Meta:
        template = "base/blocks/grid.html"


class GridBlock(StreamBlock):

    class Meta:
        template = "base/blocks/grid.html"


class SectionContent(StructBlock):
    heading = HeadingBlock(
        required=False
    )
    grid = GridBlock(
        required=False
    )
    footnote = FootnoteBlock(
        required=False
    )

    class Meta:
        label = "Contents"
        template = "base/includes/section_content.html"


class Section(StructBlock):
    content = ListBlock(
        SectionContent()
    )
    classname = CharBlock(
        required=False
    )

    class Meta:
        icon = "doc-full"
        label = "Section"
        template = "base/includes/section.html"

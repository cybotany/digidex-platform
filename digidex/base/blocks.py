from wagtail.blocks import StructBlock, CharBlock, URLBlock, StreamBlock


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
        template = "base/blocks/heading_block.html"


class FootnoteBlock(StructBlock):
    text = CharBlock(
        required=False
    )
    link = TextLink(
        required=True
    )

    class Meta:
        template = "base/blocks/footnote_block.html"


class LeftBlock(StreamBlock):

    class Meta:
        template = "base/blocks/right_block.html"


class RightBlock(StreamBlock):

    class Meta:
        template = "base/blocks/left_block.html"


class GridBlock(StreamBlock):

    class Meta:
        template = "base/blocks/grid_block.html"


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
        label = "Content"
        template = "base/includes/section_content.html"


class Section(StructBlock):
    content = SectionContent(
        required=True
    )
    classname = CharBlock(
        required=False
    )

    class Meta:
        icon = "doc-full"
        label = "Section"
        template = "base/includes/section.html"

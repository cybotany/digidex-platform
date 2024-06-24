from wagtail.blocks import ChoiceBlock, StructBlock, CharBlock, URLBlock, StreamBlock


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


class Title(StructBlock):
    text = CharBlock(
        required=True
    )
    size = ChoiceBlock(
        choices=[
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
            ("h6", "H6"),
        ],
        default="h2",
        required=False
    )

    class Meta:
        template = "base/includes/title.html"


class Subtitle(CharBlock):
    text = CharBlock(
        required=True
    )

    class Meta:
        template = "base/includes/subtitle.html"


class HeadingBlock(StructBlock):
    subtitle = Subtitle(
        classname="title",
        required=False
    )
    title = Title(
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
        icon = "doc-full"
        label = "Section"
        template = "base/includes/section_content.html"


class Section(StructBlock):
    classname = CharBlock(
        required=False
    )
    content = SectionContent(
        required=True
    )

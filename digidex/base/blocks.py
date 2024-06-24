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


class BaseSectionBlock(StructBlock):
    heading = HeadingBlock(
        required=False
    )
    footnote = FootnoteBlock(
        required=False
    )

    class Meta:
        icon = "doc-full"
        label = "Section"
        template = "base/blocks/base_section.html"


class SectionBlock(StreamBlock):
    section = BaseSectionBlock()

    class Meta:
        template = "base/blocks/section.html"

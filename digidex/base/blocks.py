from wagtail import blocks
from wagtail.images import blocks as image_blocks
from wagtail.embeds import blocks as embed_blocks

from base.constants import PREDEFINED_CSS_STYLES

class ImageFigureBlock(blocks.StructBlock):
    image = image_blocks.ImageChooserBlock(
        required=True
    )
    caption = blocks.CharBlock(
        required=False
    )
    attribution = blocks.CharBlock(
        required=False
    )

    class Meta:
        icon = "image"
        template = "base/blocks/image_figure_block.html"


class HeadingBlock(blocks.CharBlock):
    text = blocks.CharBlock(
        classname="title",
        required=True
    )
    style = blocks.ChoiceBlock(
        choices=PREDEFINED_CSS_STYLES,
        blank=True,
        required=False,
    )
    size = blocks.ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
            ("h6", "H6"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class ParagraphBlock(blocks.RichTextBlock):
    text = blocks.RichTextBlock()
    style = blocks.ChoiceBlock(
        choices=PREDEFINED_CSS_STYLES,
        blank=True,
        required=False,
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/paragraph_block.html"


class SectionBlock(blocks.StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = ParagraphBlock()
    image_block = ImageFigureBlock()
    embed_block = embed_blocks.EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

    class Meta:
        icon = "doc-full"
        template = "base/blocks/section_block.html"


class PageHeadingBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=True,
        classname="full title"
    )
    introduction = blocks.RichTextBlock(
        required=False
    )

    class Meta:
        template = 'base/blocks/page_heading_block.html'
        icon = 'title'

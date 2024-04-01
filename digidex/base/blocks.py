from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class BaseStructBlock(blocks.StructBlock):
    pass


class BaseStreamBlock(blocks.StreamBlock):
    pass


class HeadingBlock(BaseStructBlock):
    title = blocks.CharBlock(
        classname="title",
        required=True
    )
    size = blocks.ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class BaseListItemBlock(BaseStructBlock):
    text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="List item text"
    )


class BaseListBlock(blocks.ListBlock):
    pass


class ParagraphBlock(blocks.RichTextBlock):
    class Meta:
        icon = "pilcrow"
        template = "base/blocks/paragraph_block.html"


class ContentBlock(BaseStructBlock):
    """
    A generic content block for heading and body.
    """
    heading = HeadingBlock(
        max_length=50,
        help_text="Enter the heading text here"
    )
    paragraph = ParagraphBlock(
        required=False,
        help_text="Enter the body here"
    )


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(
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
        template = "base/blocks/image_block.html"


class PageBodyBlock(blocks.StreamBlock):
    heading = HeadingBlock()
    body = ParagraphBlock()
    image = ImageBlock()
    embed = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

    class Meta:
        icon = "placeholder"
        template = "base/blocks/page_body_block.html"

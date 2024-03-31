from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


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


class PageHeadingBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        classname="full",
        help_text="Enter the heading text"
    )
    paragraph = blocks.TextBlock(
        required=False,
        classname="full",
        help_text="Enter the heading subtext"
    )

    class Meta:
        icon = "placeholder"
        label = "Heading"


class BaseStreamBlock(blocks.StreamBlock):
    heading = PageHeadingBlock()
    paragraph = blocks.RichTextBlock(icon="pilcrow")
    image = ImageBlock()
    embed = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

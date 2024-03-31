from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)
    attribution = blocks.CharBlock(required=False)
    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"


class HeadingBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=True,
        classname="full",
        help_text="Enter the header text"
    )
    paragraph = blocks.TextBlock(
        required=False,
        classname="full",
        help_text="Enter the subtext"
    )

    class Meta:
        template = "base/blocks/heading_block.html"
        icon = "placeholder"
        label = "Header Section"


class BaseStreamBlock(blocks.StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = blocks.RichTextBlock(icon="pilcrow")
    image_block = ImageBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

from wagtail import blocks
from wagtail.images import blocks as img_blocks

class ImageBlock(blocks.StructBlock):
    image = img_blocks.ImageChooserBlock(
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


class LinkPageBlock(blocks.PageChooserBlock):
    class Meta:
        icon = "link"
        template = "base/blocks/link_block.html"


class LinkURLBlock(blocks.URLBlock):
    class Meta:
        icon = "link-external"
        template = "base/blocks/link_block.html"
# image_blocks.py
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)
    attribution = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"

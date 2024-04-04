from wagtail import blocks
from wagtail.images import blocks as image_blocks

class _ImageBlock(image_blocks.ImageChooserBlock):
    pass

class ImageBlock(blocks.StructBlock):
    image = _ImageBlock(
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
        template = "base/blocks/basic/image_figure_block.html"

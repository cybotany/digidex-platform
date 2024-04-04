from wagtail import blocks
from wagtail.images import blocks as image_blocks

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

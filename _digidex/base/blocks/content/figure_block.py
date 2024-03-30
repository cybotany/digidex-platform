# base/blocks/content/figure_block.py
from wagtail import blocks
from wagtail.images import blocks as image_blocks

class FigureBlock(blocks.StructBlock):
    image = image_blocks.ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False, help_text='Add a caption for the image')

    class Meta:
        template = "base/blocks/content/figure_block.html"

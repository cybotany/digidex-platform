from wagtail import blocks
# Project specific blocks
from cms.base.blocks import basic_blocks

class BannerBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    button = basic_blocks.ButtonBlock()
    lottie_animation = basic_blocks.LottieAnimationBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/banner_block.html'

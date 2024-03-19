# Project specific blocks
from cms.base.blocks import layout_blocks as _lblocks
# App specific blocks
from cms.base.blocks import composite_blocks as _cblocks
from home.blocks.partials import lottie_block

class BannerBlock(_lblocks.SectionBlock):
    title = _cblocks.HeadingBlock()
    button = _cblocks.ButtonBlock()
    lottie_animation = lottie_block.LottieBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/banner_block.html'

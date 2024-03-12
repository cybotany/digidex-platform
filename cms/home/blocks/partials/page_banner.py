# Project specific blocks
from base.blocks.basic import layout_blocks as _lblocks, \
                              composite_blocks as _cblocks
# App specific blocks
from home.blocks.partials import lottie_block

class BannerBlock(_lblocks.SectionBlock):
    title = _cblocks.HeadingBlock()
    button = _cblocks.ButtonBlock()
    lottie_animation = lottie_block.LottieBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/banner_block.html'

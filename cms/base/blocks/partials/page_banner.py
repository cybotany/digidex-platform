# Project specific blocks
from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks
from home.blocks.partials import lottie_block

class BannerBlock(_lblocks.SectionBlock):
    title = _cblocks.HeadingBlock()
    button = _cblocks.ButtonBlock()
    lottie_animation = lottie_block.LottieBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/banner_block.html'

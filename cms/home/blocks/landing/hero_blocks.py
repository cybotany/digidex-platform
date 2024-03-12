# Project specific blocks
from base.blocks.basic import basic_blocks as _bblocks,\
                              layout_blocks as _lblocks,\
                              composite_blocks as _cblocks
# App specific blocks
from home.blocks.partials import lottie_block

class HeroSectionBlock(_lblocks.SectionBlock):
    title = _cblocks.HeadingBlock()
    promotional_link = _cblocks.URLBlock(
        help_text="Optional promotional link, for example, a discount or special offer."
    )
    button = _bblocks.BaseListBlock(
        _cblocks.ButtonBlock()
    )
    lottie_animations = lottie_block.LottieBlock(
        required=False
    )

    class Meta:
        template = 'blocks/hero_section_block.html'


class FeatureIconBlock(_cblocks.URLBlock):
    pass
    class Meta:
        icon = 'pick'
        template = 'blocks/feature_icon_block.html'

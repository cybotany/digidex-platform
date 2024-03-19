# Project specific blocks
from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks
# App specific blocks
from home.blocks.partials import lottie_block

class HeroBlock(_lblocks.SectionBlock):
    heading = _cblocks.HeadingBlock()
    paragraph = _cblocks.ParagraphBlock()
    buttons = _bblocks.BaseStreamBlock(
        [
            ('button', _cblocks.ButtonBlock(label="Button")),
        ],
        required=False,
        help_text="Add buttons here"
    )
    promotional_link = _cblocks.URLBlock(
        help_text="Optional promotional link, for example, a discount or special offer."
    )
    lottie_animations = lottie_block.LottieBlock(
        required=False
    )

    class Meta:
        template = 'blocks/landing/hero_section.html'


class FeatureIconBlock(_cblocks.URLBlock):
    pass
    class Meta:
        icon = 'pick'
        template = 'blocks/feature_icon_block.html'

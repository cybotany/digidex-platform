from cms.base.blocks import basic_blocks as _bblocks,\
                            composite_blocks as _cblocks,\
                            layout_blocks as _lblocks

class TopBarPromoBlock(_bblocks.BaseStructBlock):
    message = _bblocks.BaseCharBlock(
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'


class PromoBarBlock(_lblocks.SectionBlock):
    promo = TopBarPromoBlock()
    icons = _bblocks.BaseListBlock(
        _cblocks.URLBlock()
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/base/page/header/navigation/promo_bar.html'

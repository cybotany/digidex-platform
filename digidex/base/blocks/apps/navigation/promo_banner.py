from base.blocks import basic_blocks as _bblocks,\
                            composite_blocks as _cblocks

class TopBarPromoBlock(_bblocks.BaseStructBlock):
    message = _bblocks.BaseCharBlock(
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'


class PromoBarBlock(_bblocks.SectionBlock):
    promo = TopBarPromoBlock()
    icons = _bblocks.BaseListBlock(
        _cblocks.URLBlock()
    )

    class Meta:
        icon = 'doc-full'
        template = 'base/blocks/apps/navigation/promo_bar.html'

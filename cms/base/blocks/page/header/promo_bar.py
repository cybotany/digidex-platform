from cms.base.blocks import basic_blocks as _bblocks,\
                            composite_blocks as _cblocks,\
                            layout_blocks as _lblocks

class TopBarPromoBlock(_bblocks.BaseStructBlock):
    message = _bblocks.BaseCharBlock( # top-bar/info-top-bar
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/base/page/header/navigation/promo/message.html'


class TopBarIconBlock(_bblocks.BaseStructBlock):
    icon = _cblocks.URLBlock( # top-bar/link-top-bar w-inline-block/icon-top-bar/text-top-bar
        help_text="Add links to the top bar"
    )


    class Meta:
        icon = 'doc-full'
        template = 'blocks/base/page/header/navigation/promo/icon.html'


class PromoBarBlock(_lblocks.SectionBlock):
    promo = TopBarPromoBlock()
    icons = _bblocks.BaseStreamBlock(
        TopBarIconBlock
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/base/page/header/navigation/promo_bar.html'

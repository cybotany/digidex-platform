from base.blocks import basic_blocks, composite_blocks


class TopBarPromoBlock(basic_blocks.BaseStructBlock):
    message = basic_blocks.BaseCharBlock(
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'


class PromoBarBlock(basic_blocks.SectionBlock):
    promo = TopBarPromoBlock()
    icons = basic_blocks.BaseListBlock(
        composite_blocks.URLBlock()
    )

    class Meta:
        icon = 'doc-full'
        template = 'base/blocks/apps/navigation/promo_bar.html'

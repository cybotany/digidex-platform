from base.blocks import basics, components, layouts


class TopBarPromoBlock(basics.BaseStructBlock):
    message = basics.BaseCharBlock(
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'


class PromoBarBlock(basics.SectionBlock):
    promo = TopBarPromoBlock()
    icons = basics.BaseListBlock(
        components.URLBlock()
    )

    class Meta:
        icon = 'doc-full'
        template = 'base/blocks/apps/navigation/promo_bar.html'

from digidex.base.blocks import component
from digidex.base.blocks import basic


class TopBarPromoBlock(basic.BaseStructBlock):
    message = basic.BaseCharBlock(
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'


class PromoBarBlock(basic.SectionBlock):
    promo = TopBarPromoBlock()
    icons = basic.BaseListBlock(
        component.URLBlock()
    )

    class Meta:
        icon = 'doc-full'
        template = 'base/blocks/apps/navigation/promo_bar.html'

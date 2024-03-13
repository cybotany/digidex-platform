from cms.base.blocks import basic_blocks
from base.blocks.page.header import navigation_bar, promo_bar

class PageHeaderBlock(basic_blocks.BaseStructBlock):
    promo = promo_bar.PromoBarBlock()
    navigation = navigation_bar.NavigationBarBlock()

    class Meta:
        template = "blocks/layout/page_header.html"


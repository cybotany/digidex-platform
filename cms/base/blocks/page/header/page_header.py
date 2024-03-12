from base.blocks.basic import basic_blocks
from base.blocks.page.header import navigation_bar, promo_banner

class PageHeaderBlock(basic_blocks.BaseStructBlock):
    promo = promo_banner.PromoBarBlock()
    navigation = navigation_bar.NavigationBarBlock()

    class Meta:
        template = "blocks/layout/page_header.html"


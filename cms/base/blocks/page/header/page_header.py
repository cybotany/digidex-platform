from cms.base.blocks import basic_blocks as bblocks
from base.blocks import composite_blocks as cblocks

class PageHeaderBlock(bblocks.BaseStructBlock):
    promo = cblocks.PromoBarBlock()
    navigation = cblocks.NavigationBarBlock()

    class Meta:
        template = "blocks/layout/page_header.html"


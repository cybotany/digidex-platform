from cms.base.blocks import basic_blocks as bblocks
from base.blocks import composite_blocks as cblocks

class PageHeaderBlock(bblocks.BaseStructBlock):
    promo = cblocks.PromoBarBlock()
    navigation = cblocks.NavigationBarBlock()

    class Meta:
        template = "blocks/layout/page_header.html"


class PageBodyBlock(bblocks.BaseStreamBlock):
    sections = bblocks.BaseStreamBlock(
        [
            ('section', SectionBlock()),
        ],
        min_num=1
    ) 

    class Meta:
        template = "blocks/layout/page_body.html"


class PageFooterBlock(bblocks.BaseStructBlock):
    promo = cblocks.PromoBarBlock()
    navigation = cblocks.NavigationBarBlock()

    class Meta:
        template = "blocks/layout/page_header.html"


class PageLayoutBlock(bblocks.BaseStructBlock):
    page_header = PageHeaderBlock()
    page_body = PageBodyBlock()
    page_footer = PageFooterBlock()

    class Meta:
        template = "blocks/layout/page.html"

from cms.base.blocks import basic_blocks as bblocks
from base.blocks import composite_blocks as cblocks

class GridBlock(bblocks.BaseStreamBlock):
    items = bblocks.BaseStreamBlock(
        [
            ('base_block', bblocks.BaseBlock()),
        ],
        min_num=1
    )

    class Meta:
        template = "blocks/layout/grid.html"


class ContentBlock(bblocks.BaseStructBlock):
    content_block = bblocks.BaseStreamBlock(
        [
            ('grid', GridBlock()),
            ('block', bblocks.BaseBlock()),
        ],
        max_num=1
    )

    class Meta:
        template = "blocks/layout/content.html"


class SectionBlock(bblocks.BaseStructBlock):
    content = ContentBlock()

    class Meta:
        template = "blocks/layout/section.html"


class BasePageBody(bblocks.BaseStreamBlock):
    sections = bblocks.BaseStreamBlock(
        [
            ('section', SectionBlock()),
        ],
        min_num=1
    ) 

    class Meta:
        template = "blocks/layout/page_body.html"


class PageHeaderBlock(bblocks.BaseStructBlock):
    promo = cblocks.PromoBarBlock()
    navigation = cblocks.NavigationBarBlock()

    class Meta:
        template = "blocks/layout/page_header.html"


class BasePage(bblocks.BaseStructBlock):
    page_header = PageHeaderBlock()
    page_body = BasePageBody()
    page_footer = cblocks.FooterBlock()

    class Meta:
        template = "blocks/layout/page.html"

from base.blocks.basic import basic_blocks
from base.blocks.page.header import page_header
from base.blocks.page.body import page_body
from base.blocks.page.footer import page_footer

class PageLayoutBlock(basic_blocks.BaseStructBlock):
    page_header = page_header.PageHeaderBlock()
    page_body = page_body.PageBodyBlock()
    page_footer = page_footer.PageFooterBlock()

    class Meta:
        template = "blocks/layout/page.html"

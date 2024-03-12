from base.blocks.basic import basic_blocks, layout_blocks

class PageBodyBlock(basic_blocks.BaseStreamBlock):
    sections = basic_blocks.BaseStreamBlock(
        [
            ('section', layout_blocks.SectionBlock()),
        ],
        min_num=1
    ) 

    class Meta:
        template = "blocks/layout/page_body.html"
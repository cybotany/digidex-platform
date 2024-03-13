from cms.base.blocks import basic_blocks as _bblocks,\
                            layout_blocks as _lblocks

class PageBodyBlock(_bblocks.BaseStreamBlock):
    sections = _bblocks.BaseStreamBlock(
        [
            ('section', _lblocks.SectionBlock()),
        ],
        min_num=1
    ) 

    class Meta:
        template = "blocks/layout/page_body.html"
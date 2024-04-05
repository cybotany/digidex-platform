from wagtail import blocks

from base.blocks import basic as _bblocks

class PageHeadingBlock(blocks.StructBlock):
    """
    Page Heading Block
    """
    heading = _bblocks._HeadingBlock(
        required=True
    )
    introduction = _bblocks._ParagraphBlock(
        required=False
    )

    class Meta:
        template = 'base/blocks/sections/page_heading.html'
        icon = 'title'
        label = 'Page Heading'

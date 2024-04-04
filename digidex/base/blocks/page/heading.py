from wagtail import blocks

from base.blocks.basic import image as _bblocks

class PageHeadingBlock(blocks.StructBlock):
    """
    Page Heading Block
    """
    heading = _bblocks.HeadingBlock(
        required=True
    )
    introduction = _bblocks.ParagraphBlock(
        required=False
    )

    class Meta:
        template = 'base/blocks/page/page_heading.html'
        icon = 'title'
        label = 'Page Heading'

from wagtail import blocks

from base.blocks import basic

class PageHeadingBlock(blocks.StructBlock):
    """
    Page Heading Block
    """
    heading = basic.Heading(
        required=True
    )
    introduction = basic.Paragraph(
        required=False
    )

    class Meta:
        template = 'base/blocks/sections/page_heading.html'
        icon = 'title'
        label = 'Page Heading'

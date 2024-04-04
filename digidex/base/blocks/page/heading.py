from wagtail import blocks

from base.blocks.basic import heading, paragraph

class PageHeadingBlock(blocks.StructBlock):
    """
    Page Heading Block
    """
    heading = heading._HeadingBlock(
        required=True
    )
    introduction = paragraph._ParagraphBlock(
        required=False
    )

    class Meta:
        template = 'base/blocks/page/page_heading.html'
        icon = 'title'
        label = 'Page Heading'

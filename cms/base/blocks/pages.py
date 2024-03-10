from wagtail import blocks

class PageHeadingBlock(blocks.StructBlock):
    date = blocks.DateBlock(
        classname="date-top",
        required=False
    )
    paragraph = blocks.RichTextBlock(
        classname="paragraph-top",
        required=False
    )

    class Meta:
        icon = "title"
        template = "base/blocks/page_heading_block.html"


class BasePageBlock(blocks.StreamBlock):
    heading_block = PageHeadingBlock()
    paragraph_block = blocks.RichTextBlock(icon="pilcrow")

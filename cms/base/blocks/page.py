from wagtail import blocks

class PageHeadingBlock(blocks.StructBlock):
    heading_text = blocks.RichTextBlock(
        classname="heading-top",
        required=True
    )
    paragraph = blocks.RichTextBlock(
        classname="paragraph-top",
        required=False
    )

    class Meta:
        icon = "title"
        template = "base/blocks/page/page_heading_block.html"


class BasePageBlock(blocks.StreamBlock):
    heading_block = PageHeadingBlock()
    paragraph_block = blocks.RichTextBlock(icon="pilcrow")

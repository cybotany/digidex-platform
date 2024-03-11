from wagtail import blocks

class SectionHeadingBlock(blocks.StructBlock):
    subtitle_text = blocks.RichTextBlock(
        classname="subtitle",
        required=False
    )
    subtitle_link_text = blocks.RichTextBlock(
        classname="subtitle green",
        required=False
    )
    heading_text = blocks.RichTextBlock(
        classname="heading",
        required=True
    )

    class Meta:
        icon = "title"
        template = "base/blocks/section_heading_block.html"


class BaseSectionBlock(blocks.StreamBlock):
    heading_block = SectionHeadingBlock()
    paragraph_block = blocks.RichTextBlock(
        icon="pilcrow"
    )

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

from wagtail import blocks

class HeadingBlock(blocks.CharBlock):
    heading_text = blocks.CharBlock(
        classname="title",
        required=True
    )
    size = blocks.ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
            ("h6", "H6"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class ParagraphBlock(blocks.RichTextBlock):
    content = blocks.RichTextBlock()

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/paragraph_block.html"


class PageHeadingBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    introduction = blocks.RichTextBlock()

    class Meta:
        template = "base/blocks/page_heading_block.html"
        icon = "title"

from wagtail import blocks

class _Paragraph(blocks.RichTextBlock):
    pass


class ParagraphBlock(blocks.StructBlock):
    text = _Paragraph(
        required=True
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/basic/paragraph_block.html"

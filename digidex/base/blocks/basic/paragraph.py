from wagtail import blocks

class _ParagraphBlock(blocks.RichTextBlock):
    pass


class ParagraphBlock(blocks.StructBlock):
    text = _ParagraphBlock(
        required=True
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/basic/paragraph_block.html"

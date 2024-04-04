from wagtail import blocks

class _ParagraphBlock(blocks.RichTextBlock):
    text = blocks.RichTextBlock()

    class Meta:
        icon = "pilcrow"


class ParagraphBlock(_ParagraphBlock):
    class Meta:
        template = "base/blocks/paragraph_block.html"

# base/blocks/page_content_block.py
from wagtail import blocks
from .content import FigureBlock, ButtonBlock, DigitBlock

class PageContentBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(required=False, max_length=255)
    body = blocks.RichTextBlock()
    figure = FigureBlock()
    buttons = ButtonBlock()
    digits = DigitBlock()

    class Meta:
        template = "base/blocks/page_content_block.html"

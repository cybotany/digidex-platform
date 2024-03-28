# base/blocks/page_block.py
from wagtail import blocks
from .content import FigureBlock, ButtonBlock, DigitBlock

class PageHeadingBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=100)
    text = blocks.CharBlock(required=False, max_length=255)

    class Meta:
        template = "base/blocks/heading_block.html"

class PageContentBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(required=False, max_length=255)
    paragraph = blocks.RichTextBlock()
    figure = FigureBlock()
    buttons = ButtonBlock()
    digits = DigitBlock()

    class Meta:
        template = "base/blocks/content_block.html"

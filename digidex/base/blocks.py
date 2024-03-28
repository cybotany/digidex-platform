# base/blocks.py
from wagtail import blocks
from wagtail.embeds import blocks as embed_blocks

class PageHeading(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock(required=True, max_length=255)

    class Meta:
        template = "base/blocks/page/heading_block.html"


class PageContent(blocks.StreamBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image = FigureBlock()
    buttons = ButtonBlock()
    digits = DigitBlock()
    embeded_object = embed_blocks.EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media"
    )

    class Meta:
        template = "base/blocks/page/content_block.html"

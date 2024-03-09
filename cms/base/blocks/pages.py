from wagtail import blocks
from wagtail.images import blocks as i_blocks
from wagtail.embeds import blocks as e_blocks

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
    image_block = i_blocks.ImageBlock()
    embed_block = e_blocks.EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

from wagtail import blocks
from wagtail.images import blocks as i_blocks
from wagtail.embeds import blocks as e_blocks

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
        classname="heading-top",
        required=True
    )

    class Meta:
        icon = "title"
        template = "base/blocks/section_heading_block.html"


class BaseSectionBlock(blocks.StreamBlock):
    heading_block = SectionHeadingBlock()
    paragraph_block = blocks.RichTextBlock(icon="pilcrow")
    image_block = i_blocks.ImageBlock()
    embed_block = e_blocks.EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

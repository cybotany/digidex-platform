from wagtail import blocks
from wagtail.images import blocks as img_blocks

class ImageBlock(blocks.StructBlock):
    image = img_blocks.ImageChooserBlock(
        required=True
    )
    caption = blocks.CharBlock(
        required=False
    )
    attribution = blocks.CharBlock(
        required=False
    )

    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"


class LinkPageBlock(blocks.PageChooserBlock):
    class Meta:
        icon = "link"
        template = "base/blocks/link_block.html"


class LinkURLBlock(blocks.URLBlock):
    class Meta:
        icon = "link-external"
        template = "base/blocks/link_block.html"


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

from wagtail import blocks
from wagtail.embeds import blocks as embed_blocks
from wagtail.images import blocks as img_blocks


class LinkPageBlock(blocks.PageChooserBlock):
    classname = "link-block base-inline-block"
    required = False


class LinkURLBlock(blocks.URLBlock):
    classname = "link-block base-inline-block"
    required = False


class HeadingBlock(blocks.CharBlock):
    classname="heading"
    required=True


class ParagraphBlock(blocks.RichTextBlock):
    classname="paragraph"
    required=True


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


class LearnMoreBlock(blocks.StructBlock):
    link = LinkPageBlock(
        classname="link-block",
        required=True
    )
    text = blocks.CharBlock(
        classname="text-link",
        default="Learn more",
        required=True
    )
    icon = img_blocks.ImageChooserBlock(
        classname="icon-link",
        required=True
    )

    class Meta:
        icon = "doc-full"
        template = "base/blocks/learn_more_block.html"

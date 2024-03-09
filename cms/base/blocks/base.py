from wagtail.core import blocks
from wagtail.images import blocks as i_blocks
from wagtail.embeds import blocks as e_blocks

class ImageBlock(blocks.StructBlock):
    image = i_blocks.ImageChooserBlock(
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


class LottieAnimationBlock(blocks.StructBlock):
    animation_src = blocks.URLBlock(
        required=True,
        help_text="URL to the Lottie animation JSON file."
    )
    loop = blocks.BooleanBlock(
        required=False,
        default=False
    )
    autoplay = blocks.BooleanBlock(
        required=False,
        default=False
    )
    # Add other fields as necessary...

    class Meta:
        template = "blocks/lottie_animation_block.html"


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
        template = "base/blocks/page_heading_block.html"


class PageHeadingBlock(SectionHeadingBlock):
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


class StepBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        max_length=100
    )
    description = blocks.TextBlock(
        required=True
    )
    icon = e_blocks.ImageChooserBlock(
        required=False
    )

    class Meta:
        icon = 'list-ul'
        template = 'blocks/step_block.html'


class BaseStreamBlock(blocks.StreamBlock):
    heading_block = SectionHeadingBlock()
    paragraph_block = blocks.RichTextBlock(icon="pilcrow")
    image_block = ImageBlock()
    embed_block = e_blocks.EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

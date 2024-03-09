from wagtail import blocks
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

    class Meta:
        template = "base/blocks/lottie_animation_block.html"


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
        template = 'base/blocks/step_block.html'

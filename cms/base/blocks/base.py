from wagtail import blocks
from wagtail.images import blocks as i_blocks

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
    direction = blocks.IntegerBlock(
        default=1,
        help_text="Direction of the animation playback."
    )
    autoplay = blocks.BooleanBlock(
        required=False,
        default=False
    )
    renderer = blocks.ChoiceBlock(
        choices=[('svg', 'SVG'), ('canvas', 'Canvas'), ('html', 'HTML')],
        default='svg',
        help_text="Rendering mode for the animation."
    )
    default_duration = blocks.FloatBlock(
        required=False,
        help_text="Default duration in seconds."
    )
    duration = blocks.FloatBlock(
        required=False,
        default=0,
        help_text="Animation duration in seconds, overrides default duration."
    )

    class Meta:
        template = "base/blocks/lottie_animation_block.html"


class LottieBlock(blocks.StructBlock):
    lottie_animation_1 = LottieAnimationBlock()
    lottie_animation_2 = LottieAnimationBlock()
    lottie_animation_2_blur = LottieAnimationBlock()

    class Meta:
        template = 'blocks/lottie_block.html'


class LinkBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(required=True, help_text="Select an icon for the link")
    text = blocks.CharBlock(required=True, max_length=255, help_text="Enter the display text for the link")
    url = blocks.URLBlock(required=False, help_text="Enter a URL for the link (optional)")

    class Meta:
        icon = 'link'
        template = 'blocks/top_bar_link_block.html'


class PromoBlock(blocks.StructBlock):
    message = blocks.CharBlock(required=True, max_length=255, help_text="Enter the promotional message")

    class Meta:
        icon = 'doc-full'
        template = 'blocks/top_bar_promo_block.html'


class TopBarBlock(blocks.StructBlock):
    promo = PromoBlock(
        help_text="Set the promotional message for the top bar"
    )
    links = blocks.ListBlock(
        LinkBlock(help_text="Add links to the top bar")
    )

    class Meta:
        icon = 'edit'
        template = 'blocks/top_bar_block.html'

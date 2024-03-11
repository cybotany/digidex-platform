from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class BaseTitleBlock(blocks.StructBlock):
    """
    A base block for titles and subtitles, with an optional CSS class for styling.
    """
    title = blocks.CharBlock(required=True, max_length=255, help_text="Enter the title")
    subtitle = blocks.CharBlock(required=False, max_length=255, help_text="Enter the subtitle (optional)")
    css_class = blocks.CharBlock(required=False, max_length=255, help_text="CSS class for styling (optional)")

    class Meta:
        icon = 'title'
        label = 'Title'


class IconBlock(blocks.StructBlock):
    """
    A base block for representing icons across different blocks.
    """
    image = ImageChooserBlock(
        required=True,
        help_text="Select an icon image"
    )
    alt_text = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Alt text for the icon (optional)"
    )

    class Meta:
        icon = 'image'
        label = 'Icon'

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(
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
        template = "blocks/image_block.html"


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
        choices=[
            ('svg', 'SVG'),
            ('canvas', 'Canvas'),
            ('html', 'HTML')
        ],
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
        template = "blocks/lottie_animation_block.html"


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


class ActionButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the button text"
    )
    button_url = blocks.URLBlock(
        required=True,
        help_text="Enter the button URL"
    )
    button_style = blocks.ChoiceBlock(
        choices=[
            ('outline', 'Outline'),
            ('fill', 'Fill'),
        ], icon='choice', help_text="Select the button style")

    class Meta:
        icon = 'plus'
        template = 'blocks/action_button_block.html'


class LinkBlock(blocks.StructBlock):
    icon = IconBlock()
    text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the display text for the link"
    )
    url = blocks.URLBlock(
        required=False,
        help_text="Enter a URL for the link (optional)"
    )

    class Meta:
        icon = 'link'
        template = 'blocks/top_bar_link_block.html'

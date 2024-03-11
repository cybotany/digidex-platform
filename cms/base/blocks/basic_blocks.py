from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class BaseTitleBlock(blocks.StructBlock):
    """
    A base block for titles and subtitles, with an optional CSS class for styling.
    """
    title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the title"
    )
    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Enter the subtitle (optional)"
    )
    css_class = blocks.CharBlock(
        required=False,
        choices=[
            ('default', 'Default'),
            ('highlight', 'Highlight'),
            ('large', 'Large')
        ],
        default='default',
        help_text="CSS class for styling (optional)"
    )

    class Meta:
        icon = 'title'
        label = 'Title'
        template = 'blocks/title_block.html'


class BaseIconBlock(blocks.StructBlock):
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
    #icon = blocks.ChoiceBlock(
    #    choices=get_dynamic_icon_choices(),
    #    required=True,
    #    help_text="Select an icon"
    #)

    class Meta:
        icon = 'image'
        label = 'Icon'
        template = 'blocks/icon_block.html'

class BaseImageBlock(blocks.StructBlock):
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
        label = "Image"
        template = "blocks/image_block.html"


class BaseURLBlock(blocks.StructBlock):
    url = blocks.URLBlock(
        required=True,
        help_text="Enter the URL"
    )
    title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the title"
    )
    target = blocks.ChoiceBlock(
        required=False,
        choices=[
            ('_self', 'Same window'),
            ('_blank', 'New window')
        ],
        help_text="Where the link should open",
        default='_self'
    )
    
    class Meta:
        icon = 'link'
        label = 'URL'
        template = 'blocks/base_url_block.html'


class BaseLinkBlock(blocks.StructBlock):
    icon = BaseIconBlock()
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
    aspect_ratio = blocks.CharBlock(
        required=False,
        max_length=10,
        help_text="Aspect ratio (e.g., '16:9')",
        default='16:9'
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
        ],
        icon='choice',
        help_text="Select the button style"
    )

    class Meta:
        icon = 'plus'
        template = 'blocks/action_button_block.html'

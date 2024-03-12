from base.blocks import basic_blocks as bblocks

class ImageBlock(bblocks.BaseStructBlock):
    image = bblocks.BaseImageBlock()
    caption = bblocks.BaseCharBlock(
        required=False
    )
    attribution = bblocks.BaseCharBlock(
        required=False
    )
    alt_text = bblocks.BaseCharBlock(
        required=False,
        help_text="Alt text for the icon (optional)"
    )

    class Meta:
        icon = "image"
        label = "Image"
        template = "blocks/image_block.html"


class URLBlock(bblocks.BaseStructBlock):
    icon = bblocks.BaseImageBlock(
        required=False,
        help_text="Optional: Select an icon image"
    )
    text = bblocks.BaseCharBlock(
        help_text="Enter the link title or text"
    )
    url = bblocks.BaseURLBlock(
        required=True,
        help_text="Enter the URL"
    )
    target = bblocks.BaseChoiceBlock(
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
        label = 'Enhanced URL'
        template = 'blocks/base_url_block.html'


class ButtonBlock(bblocks.BaseStructBlock):
    button_style = bblocks.BaseChoiceBlock(
        choices=[
            ('outline', 'Outline'),
            ('fill', 'Fill'),
        ],
        icon='choice',
        help_text="Select the button style"
    )

    class Meta:
        icon = 'plus'
        template = 'blocks/button_block.html'


class TitleBlock(bblocks.BaseStructBlock):
    """
    A base block for titles and subtitles, with an optional CSS class for styling.
    """
    title = bblocks.BaseCharBlock(
        help_text="Enter the title"
    )
    subtitle = bblocks.BaseCharBlock(
        required=False,
        help_text="Enter the subtitle (optional)"
    )

    class Meta:
        icon = 'title'
        label = 'Title'
        template = 'blocks/title_block.html'


class TextContentBlock(bblocks.BaseStructBlock):
    title = TitleBlock()
    body = bblocks.BaseTextBlock(
        help_text="Enter the section body text"
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/text_content_block.html'


class LottieAnimationBlock(bblocks.BaseStructBlock):
    animation_src = bblocks.BaseURLBlock(
        help_text="URL to the Lottie animation JSON file."
    )
    loop = bblocks.BaseBooleanBlock(
        required=False,
        default=False
    )
    direction = bblocks.BaseIntegerBlock(
        default=1,
        help_text="Direction of the animation playback."
    )
    autoplay = bblocks.BaseBooleanBlock(
        required=False,
        default=False
    )
    renderer = bblocks.BaseChoiceBlock(
        choices=[
            ('svg', 'SVG'),
            ('canvas', 'Canvas'),
            ('html', 'HTML')
        ],
        default='svg',
        help_text="Rendering mode for the animation."
    )
    aspect_ratio = bblocks.BaseCharBlock(
        required=False,
        max_length=10,
        help_text="Aspect ratio (e.g., '16:9')",
        default='16:9'
    )
    default_duration = bblocks.BaseFloatBlock(
        required=False,
        help_text="Default duration in seconds."
    )
    duration = bblocks.BaseFloatBlock(
        required=False,
        default=0,
        help_text="Animation duration in seconds, overrides default duration."
    )

    class Meta:
        template = "blocks/lottie_animation_block.html"


class LottieBlock(bblocks.BaseStructBlock):
    lottie_animation_1 = LottieAnimationBlock()
    lottie_animation_2 = LottieAnimationBlock()
    lottie_animation_2_blur = LottieAnimationBlock()

    class Meta:
        template = 'blocks/lottie_block.html'

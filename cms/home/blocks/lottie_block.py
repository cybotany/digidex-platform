from base.blocks import basic_blocks as bblocks

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

from base.blocks.basic import basic_blocks as _bblocks

class LottieAnimationBlock(_bblocks.BaseStructBlock):
    animation_src = _bblocks.BaseURLBlock(
        help_text="URL to the Lottie animation JSON file."
    )
    loop = _bblocks.BaseBooleanBlock(
        required=False,
        default=False
    )
    direction = _bblocks.BaseIntegerBlock(
        default=1,
        help_text="Direction of the animation playback."
    )
    autoplay = _bblocks.BaseBooleanBlock(
        required=False,
        default=False
    )
    renderer = _bblocks.BaseChoiceBlock(
        choices=[
            ('svg', 'SVG'),
            ('canvas', 'Canvas'),
            ('html', 'HTML')
        ],
        default='svg',
        help_text="Rendering mode for the animation."
    )
    aspect_ratio = _bblocks.BaseCharBlock(
        required=False,
        max_length=10,
        help_text="Aspect ratio (e.g., '16:9')",
        default='16:9'
    )
    default_duration = _bblocks.BaseFloatBlock(
        required=False,
        help_text="Default duration in seconds."
    )
    duration = _bblocks.BaseFloatBlock(
        required=False,
        default=0,
        help_text="Animation duration in seconds, overrides default duration."
    )

    class Meta:
        template = "blocks/lottie_animation_block.html"


class LottieBlock(_bblocks.BaseStructBlock):
    lottie_animation_1 = LottieAnimationBlock()
    lottie_animation_2 = LottieAnimationBlock()
    lottie_animation_2_blur = LottieAnimationBlock()

    class Meta:
        template = 'blocks/lottie_block.html'

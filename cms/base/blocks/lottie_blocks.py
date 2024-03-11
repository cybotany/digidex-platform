# lottie_blocks.py
from wagtail.core import blocks

class LottieAnimationBlock(blocks.StructBlock):
    animation_src = blocks.URLBlock(required=True, help_text="URL to the Lottie animation JSON file.")
    loop = blocks.BooleanBlock(required=False, default=False)
    direction = blocks.IntegerBlock(default=1, help_text="Direction of the animation playback.")
    autoplay = blocks.BooleanBlock(required=False, default=False)
    renderer = blocks.ChoiceBlock(choices=[('svg', 'SVG'), ('canvas', 'Canvas'), ('html', 'HTML')], default='svg', help_text="Rendering mode for the animation.")
    default_duration = blocks.FloatBlock(required=False, help_text="Default duration in seconds.")
    duration = blocks.FloatBlock(required=False, default=0, help_text="Animation duration in seconds, overrides default duration.")

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

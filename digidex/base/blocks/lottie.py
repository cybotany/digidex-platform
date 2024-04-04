from wagtail import blocks
from wagtail.documents import blocks as doc_blocks

from base.blocks import basic as _bblocks

class _LottieAnimationBlock(blocks.StructBlock):
    file = doc_blocks.DocumentChooserBlock(
        required=True,
        help_text="Select the Lottie JSON file."
    )
    loop = blocks.BooleanBlock(
        required=False,
        help_text="Enable to loop the animation."
    )
    autoplay = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Enable to autoplay the animation."
    )
    duration = blocks.FloatBlock(
        required=False,
        help_text="Duration of the animation in seconds.",
        default=0
    )
    direction = blocks.ChoiceBlock(
        choices=[
            (1, "Normal"),
            (-1, "Reverse")
        ],
        default=1,
        help_text="Play animation in normal or reverse direction."
    )
    renderer = blocks.ChoiceBlock(
        choices=[
            ("svg", "SVG"),
            ("canvas", "Canvas"),
            ("html", "HTML")
        ],
        default="svg",
        help_text="Rendering mode of the animation."
    )
    blurred = blocks.BooleanBlock()


class LottieBlock(blocks.ListBlock):
    """
    A ListBlock that allows for 0 to 3 _LottieAnimationBlocks.
    """

    def __init__(self, **kwargs):
        super().__init__(_LottieAnimationBlock(), **kwargs)

    class Meta:
        label = 'Lottie Animations'
        template = 'base/blocks/lottie/base_block.html'


class LottieFeatureBlock(blocks.StructBlock):
    widget_id = blocks.CharBlock(
        required=False,
        help_text="Unique widget identifier for JS/CSS"
    )

    icon = _bblocks._ImageBlock(
        required=True,
        help_text="Feature icon"
    )
    text = blocks.TextBlock(
        required=True,
        help_text="Feature description"
    )


class FeaturesBlock(blocks.ListBlock):

    def __init__(self, **kwargs):
        super().__init__(LottieFeatureBlock(), **kwargs)

    class Meta:
        label = 'Lottie Features'
        template = 'base/blocks/lottie/features_block.html'

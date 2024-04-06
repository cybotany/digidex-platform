from wagtail import blocks
from wagtail.documents import blocks as doc_blocks

from base.blocks import basic

class VerticalLines(blocks.IntegerBlock):
    pass


class HorizontalLines(blocks.IntegerBlock):
    pass


class LottieLines(blocks.StructBlock):
    vertical = VerticalLines(
        required=False,
        help_text="Number of vertical lines."
    )
    horizontal = HorizontalLines(
        required=False,
        help_text="Number of horizontal lines."
    )

    class Meta:
        label = 'Lottie Animations'
        template = 'base/blocks/lottie/line_block.html'


class Animation(blocks.StructBlock):
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
    blurred = blocks.BooleanBlock(
        required=False
    )


class LottieAnimation(blocks.ListBlock):
    """
    A ListBlock that allows for 0 to 3 _LottieAnimationBlocks.
    """

    def __init__(self, **kwargs):
        super().__init__(Animation(), **kwargs)

    class Meta:
        label = 'Lottie Animations'
        template = 'base/blocks/lottie/animation_block.html'


class Feature(blocks.StructBlock):
    widget_id = blocks.CharBlock(
        required=False,
        help_text="Unique widget identifier for JS/CSS"
    )

    icon = basic.ImageBlock(
        required=True,
        help_text="Feature icon"
    )
    text = blocks.TextBlock(
        required=False,
        help_text="Feature description"
    )


class FeatureList(blocks.ListBlock):

    def __init__(self, **kwargs):
        super().__init__(Feature(), **kwargs)

    class Meta:
        label = 'Lottie Features'
        template = 'base/blocks/lottie/feature_block.html'


class Lottie(blocks.StructBlock):
    lines = LottieLines()
    animation = LottieAnimation() 
    features = FeatureList()

    class Meta:
        template = "base/blocks/lottie/base.html"

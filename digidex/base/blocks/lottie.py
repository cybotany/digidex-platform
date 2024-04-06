from base.blocks import basic

class LottieLines(basic.BasicStructBlock):
    """
    PLACEHOLDER
    """
    vertical = basic.BasicIntegerBlock(
        required=False,
        help_text="Number of vertical lines."
    )
    horizontal = basic.BasicIntegerBlock(
        required=False,
        help_text="Number of horizontal lines."
    )

    class Meta:
        label = 'Lottie Lines'
        template = 'base/blocks/lottie/line_block.html'


class Animation(basic.BasicStructBlock):
    """
    PLACEHOLDER
    """
    file = basic.BasicDocumentBlock(
        required=True,
        help_text="Select the Lottie JSON file."
    )
    loop = basic.BasicBooleanBlock(
        required=False,
        help_text="Enable to loop the animation."
    )
    autoplay = basic.BasicBooleanBlock(
        required=False,
        default=True,
        help_text="Enable to autoplay the animation."
    )
    duration = basic.BasicFloatBlock(
        required=False,
        help_text="Duration of the animation in seconds.",
        default=0
    )
    direction = basic.BasicChoiceBlock(
        choices=[
            (1, "Normal"),
            (-1, "Reverse")
        ],
        default=1,
        help_text="Play animation in normal or reverse direction."
    )
    renderer = basic.BasicChoiceBlock(
        choices=[
            ("svg", "SVG"),
            ("canvas", "Canvas"),
            ("html", "HTML")
        ],
        default="svg",
        help_text="Rendering mode of the animation."
    )
    blurred = basic.BasicBooleanBlock(
        required=False
    )


class LottieAnimation(basic.BasicListBlock):
    """
    PLACEHOLDER
    """
    def __init__(self, **kwargs):
        super().__init__(Animation(), **kwargs)

    class Meta:
        label = 'Lottie Animations'
        template = 'base/blocks/lottie/animation_block.html'


class Feature(basic.BasicStructBlock):
    """
    PLACEHOLDER
    """
    icon = basic.BasicIconBlock()
    text = basic.BasicTextBlock()
    style = basic.BasicCharBlock(
        default="",
        required=False,
        help_text="Unique css identifier for animation."
    )


class FeatureList(basic.BasicListBlock):
    """
    PLACEHOLDER
    """
    def __init__(self, **kwargs):
        super().__init__(Feature(), **kwargs)

    class Meta:
        label = 'Lottie Features'
        template = 'base/blocks/lottie/feature_block.html'

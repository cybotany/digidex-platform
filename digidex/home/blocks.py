from base import blocks


class LottieFeature(blocks.BasicStructBlock):
    icon = blocks.BasicImageBlock()
    text = blocks.BasicTextBlock()
    style = blocks.BasicCharBlock(
        default="",
        required=False,
        help_text="Unique css identifier for animation."
    )


class LottieFeatureList(blocks.BasicListBlock):
    def __init__(self, **kwargs):
        super().__init__(LottieFeature(), **kwargs)

    class Meta:
        template = 'base/blocks/lottie/feature_block.html'


class InformationBlock(blocks.BasicStructBlock):
    text = blocks.BasicTextBlock()
    icon = blocks.BasicImageBlock()
    link = blocks.BasicInternalLinkBlock()

    class Meta:
        template = "home/blocks/information_block.html"


class HeroBlock(blocks.BasicStructBlock):
    information = InformationBlock()
    heading = blocks.BasicHeadingBlock()
    paragraph = blocks.BasicParagraphBlock()

    class Meta:
        template = "home/blocks/hero_block.html"


class HeroLottie(blocks.BasicStructBlock):
    lines = blocks.LottieLines()
    animation = blocks.LottieAnimation() 
    features = LottieFeatureList()

    class Meta:
        template = "home/blocks/hero_lottie.html"

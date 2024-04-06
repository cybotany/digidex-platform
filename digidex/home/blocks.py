from base.blocks import basic, lottie


class InformationBlock(basic.BasicStructBlock):
    text = basic.BasicTextBlock()
    icon = basic.BasicIconBlock()
    link = basic.BasicInternalLinkBlock()

    class Meta:
        template = "home/blocks/information_block.html"


class HeroBlock(basic.BasicStructBlock):
    information = InformationBlock()
    heading = basic.BasicHeadingBlock()
    paragraph = basic.BasicParagraphBlock()
    cta = basic.BasicButtonBlock()

    class Meta:
        template = "home/blocks/hero_block.html"


class HeroLottie(basic.BasicStructBlock):
    lines = lottie.LottieLines()
    animation = lottie.LottieAnimation() 
    features = lottie.FeatureList()

    class Meta:
        template = "home/blocks/hero_lottie.html"

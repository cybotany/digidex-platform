from wagtail import blocks

from base.blocks import basic, lottie


class InformationBlock(basic.BasicStructBlock):
    text = basic.TextBlock()
    icon = basic.IconBlock()
    link = blocks.PageChooserBlock()

    class Meta:
        template = "home/blocks/information_block.html"


class HeroBlock(basic.BasicStructBlock):
    information = InformationBlock()
    heading = basic.HeadingBlock()
    paragraph = basic.ParagraphBlock()
    cta = basic.ButtonBlock()

    class Meta:
        template = "home/blocks/hero_block.html"


class HeroLottie(basic.BasicStructBlock):
    lines = lottie.LottieLines()
    animation = lottie.LottieAnimation() 
    features = lottie.FeatureList()

    class Meta:
        template = "home/blocks/hero_lottie.html"

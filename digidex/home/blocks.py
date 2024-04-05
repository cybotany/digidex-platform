from base.blocks import basic, lottie

class HeroBlock(basic.BasicBlock):
    heading = basic.Heading()
    paragraph = basic.Paragraph()
    button = basic.ButtonBlock()

    class Meta:
        icon = "placeholder"
        template = "home/blocks/hero_block.html"


class HeroGrid(basic.StructGrid):
    cta = HeroBlock()
    lottie = lottie.Lottie()

from base.blocks import basic, lottie

class HeroBlock(basic.BasicBlock):
    heading = basic.Heading()
    paragraph = basic.Paragraph()
    button = basic.ButtonBlock()


class HeroGrid(basic.StructGrid):
    block = HeroBlock()
    lottie = lottie.Lottie()

    class Meta:
        icon = "placeholder"
        template = "home/blocks/hero_grid.html"

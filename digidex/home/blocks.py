from base.blocks import basic, lottie

class HeroSection(basic.Section):
    heading = basic.Heading()
    introduction = basic.Paragraph()
    button = basic.ButtonBlock()
    lottie = lottie.Lottie()

    class Meta:
        icon = "placeholder"
        template = "home/blocks/hero.html"

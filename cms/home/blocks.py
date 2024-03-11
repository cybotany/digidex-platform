from wagtail import blocks
# Project specifice imports
from base.blocks import base, section, page

class HeroSection(section.BaseSectionBlock):
    lottie = base.LottieBlock()

    class Meta:
        template = "home/blocks/landing/hero_section.html"


class HowItWorksSection(section.BaseSectionBlock):
    paragraph = blocks.TextBlock(
        required=True
    )
    steps = blocks.ListBlock(
        blocks.StepBlock()
    )

    class Meta:
        template = 'home/blocks/landing/how_it_works_block.html'
        icon = 'snippet'


class CallToActionSection(section.BaseSectionBlock):
    lottie = base.LottieBlock()

    class Meta:
        template = "home/blocks/landing/call_to_action_section.html"

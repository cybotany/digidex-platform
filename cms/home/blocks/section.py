from wagtail import blocks
# Project specifice imports
from base.blocks import base, section

class HeroSection(section.BaseSectionBlock):
    lottie_animation_1 = base.LottieAnimationBlock()
    lottie_animation_2 = base.LottieAnimationBlock()

    class Meta:
        template = "home/blocks/hero_section.html"


class HowItWorksSection(section.BaseSectionBlock):
    paragraph = blocks.TextBlock(
        required=True
    )
    steps = blocks.ListBlock(
        base.StepBlock()
    )

    class Meta:
        template = 'home/blocks/how_it_works_block.html'
        icon = 'snippet'


class CallToActionSection(section.BaseSectionBlock):
    lottie_animation_1 = base.LottieAnimationBlock()
    lottie_animation_2 = base.LottieAnimationBlock()

    class Meta:
        template = "home/blocks/call_to_action_section.html"

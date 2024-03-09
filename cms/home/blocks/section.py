from cms.base.blocks import page, section
from wagtail import blocks

from base.blocks import base


class HeroSection(section.BaseSectionBlock):
    lottie_animation_1 = base.LottieAnimationBlock()
    lottie_animation_2 = base.LottieAnimationBlock()

    class Meta:
        template = "base/blocks/hero_section.html"


class HowItWorksSection(section.BaseSectionBlock):
    paragraph = blocks.TextBlock(
        required=True
    )
    steps = blocks.ListBlock(
        base.StepBlock()
    )

    class Meta:
        template = 'base/blocks/how_it_works_block.html'
        icon = 'snippet'


class CallToActionSection(section.BaseSectionBlock):
    lottie_animation_1 = base.LottieAnimationBlock()
    lottie_animation_2 = base.LottieAnimationBlock()

    class Meta:
        template = "base/blocks/call_to_action_section.html"

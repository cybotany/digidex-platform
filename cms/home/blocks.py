from cms.base.blocks import blocks
from wagtail import blocks
# Project specifice imports
from cms.base.blocks import sections

class HeroSection(sections.BaseSectionBlock):
    lottie_animation_1 = blocks.LottieAnimationBlock()
    lottie_animation_2 = blocks.LottieAnimationBlock()

    class Meta:
        template = "home/blocks/landing/hero_section.html"


class HowItWorksSection(sections.BaseSectionBlock):
    paragraph = blocks.TextBlock(
        required=True
    )
    steps = blocks.ListBlock(
        blocks.StepBlock()
    )

    class Meta:
        template = 'home/blocks/landing/how_it_works_block.html'
        icon = 'snippet'


class CallToActionSection(sections.BaseSectionBlock):
    lottie_animation_1 = blocks.LottieAnimationBlock()
    lottie_animation_2 = blocks.LottieAnimationBlock()

    class Meta:
        template = "home/blocks/landing/call_to_action_section.html"

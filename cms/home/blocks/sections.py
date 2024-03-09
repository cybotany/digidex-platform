


class HeroSection(BaseSectionBlock):
    lottie_animation_1 = LottieAnimationBlock()
    lottie_animation_2 = LottieAnimationBlock()

    class Meta:
        template = "base/blocks/hero_section.html"


class HowItWorksSection(BaseSectionBlock):
    paragraph = blocks.TextBlock(
        required=True
    )
    steps = blocks.ListBlock(
        StepBlock()
    )

    class Meta:
        template = 'base/blocks/how_it_works_block.html'
        icon = 'snippet'


class CallToActionSection(BaseSectionBlock):
    lottie_animation_1 = LottieAnimationBlock()
    lottie_animation_2 = LottieAnimationBlock()

    class Meta:
        template = "base/blocks/call_to_action_section.html"

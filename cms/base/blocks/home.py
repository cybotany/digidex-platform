from wagtail.core import blocks as core_blocks
# Project specific imports
from base.blocks import base

class CallToActionBlock(core_blocks.StructBlock):
    subtitle = core_blocks.CharBlock(
        required=True
    )
    heading = core_blocks.CharBlock(
        required=True
    )
    lottie_animation_1 = base.LottieAnimationBlock()
    lottie_animation_2 = base.LottieAnimationBlock()
    # Define other fields or animations as necessary...

    class Meta:
        template = "blocks/call_to_action_block.html"

class HowItWorksBlock(base.BaseStreamBlock):
    subtitle = core_blocks.CharBlock(
        required=True,
        max_length=100
    )
    heading = core_blocks.CharBlock(
        required=True,
        max_length=200
    )
    paragraph = core_blocks.TextBlock(
        required=True
    )
    steps = core_blocks.ListBlock(
        base.StepBlock()
    )

    class Meta:
        template = 'blocks/how_it_works_block.html'
        icon = 'snippet'


class CallToActionBlock(core_blocks.StructBlock):
    subtitle = core_blocks.CharBlock(
        required=True
    )
    heading = core_blocks.CharBlock(
        required=True
    )
    lottie_animation_1 = base.LottieAnimationBlock()
    lottie_animation_2 = base.LottieAnimationBlock()
    # Define other fields or animations as necessary...

    class Meta:
        template = "blocks/call_to_action_block.html"

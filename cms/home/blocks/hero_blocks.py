from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class HeroSectionBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    promotional_link = basic_blocks.BaseURLBlock(
        help_text="Optional promotional link, for example, a discount or special offer."
    )
    primary_action_button = basic_blocks.ActionButtonBlock(
        help_text="Primary action button, e.g., 'Get Started'."
    )
    secondary_action_button = basic_blocks.BaseURLBlock(
        help_text="Secondary action button, typically for support or contact, including an icon."
    )
    lottie_animations = basic_blocks.LottieBlock(
        required=False
    )

    class Meta:
        template = 'blocks/hero_section_block.html'


class FeatureIconBlock(blocks.StructBlock):
    icon = basic_blocks.BaseURLBlock()
    content = basic_blocks.TextContentBlock()

    class Meta:
        icon = 'pick'
        template = 'blocks/feature_icon_block.html'

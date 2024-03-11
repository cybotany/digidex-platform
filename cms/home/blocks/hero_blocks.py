from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class HeroSectionBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    promotional_link = basic_blocks.BaseLinkBlock(
        help_text="Optional promotional link, for example, a discount or special offer."
    )
    primary_action_button = basic_blocks.ActionButtonBlock(
        help_text="Primary action button, e.g., 'Get Started'."
    )
    secondary_action_button = basic_blocks.BaseLinkBlock(
        help_text="Secondary action button, typically for support or contact, including an icon."
    )
    lottie_animations = basic_blocks.LottieBlock(
        required=False
    )

    class Meta:
        template = 'blocks/hero_section_block.html'


class FeatureIconBlock(blocks.StructBlock):
    icon = basic_blocks.BaseIconBlock()
    title = basic_blocks.BaseTitleBlock()
    description = blocks.TextBlock(
        required=True,
        help_text="Short description of the feature"
    )

    class Meta:
        icon = 'pick'
        template = 'blocks/feature_icon_block.html'

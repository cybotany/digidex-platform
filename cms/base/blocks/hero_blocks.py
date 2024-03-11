from wagtail import blocks
from wagtail.images import blocks as i_blocks

class HeroSectionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255, help_text="Main heading of the hero section")
    subtitle = blocks.TextBlock(required=False, help_text="Subtitle or a short paragraph")
    promotional_link = LinkBlock(help_text="Optional promotional link")
    buttons = blocks.ListBlock(ActionButtonBlock(), help_text="Add one or more action buttons")
    lottie_animations = blocks.StructBlock([
        ('animation_1', LottieAnimationBlock(required=False)),
        ('animation_2', LottieAnimationBlock(required=False)),
        ('animation_2_blur', LottieAnimationBlock(required=False)),
    ], help_text="Lottie animations for the hero section")

    class Meta:
        template = 'blocks/hero_section_block.html'


class FeatureIconBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(required=True, help_text="Select a feature icon")
    title = blocks.CharBlock(required=True, max_length=255, help_text="Feature title")
    description = blocks.TextBlock(required=True, help_text="Short description of the feature")

    class Meta:
        icon = 'pick'
        template = 'blocks/feature_icon_block.html'

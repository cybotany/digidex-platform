from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class TextContentBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    body = blocks.TextBlock(
        required=True,
        help_text="Enter the section body text"
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/text_content_block.html'


class StatisticItemBlock(blocks.StructBlock):
    icon = basic_blocks.BaseIconBlock()
    number = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Statistic number"
    )
    description = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Statistic description"
    )
    style = blocks.ChoiceBlock(
        required=False,
        choices=[
            ('default', 'Default'),
            ('green', 'Green'),
        ],
        help_text="Statistic style",
        default='default')

    class Meta:
        icon = 'pick'
        template = 'blocks/statistic_item_block.html'


class StatisticsGridBlock(blocks.StructBlock):
    statistics = blocks.ListBlock(
        StatisticItemBlock(help_text="Add statistics")
    )

    class Meta:
        icon = 'grid'
        template = 'blocks/statistics_grid_block.html'


class FeaturedSectionBlock(blocks.StructBlock):
    lottie_animations = blocks.StructBlock(
        [
            ('animation_1', basic_blocks.LottieAnimationBlock(required=False)),
            ('animation_2', basic_blocks.LottieAnimationBlock(required=False)),
            ('animation_2_blur', basic_blocks.LottieAnimationBlock(required=False)),
        ],
        help_text="Lottie animations for the hero section"
    )
    lottie_animation = basic_blocks.LottieAnimationBlock()
    text_content = TextContentBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/featured_section_block.html'

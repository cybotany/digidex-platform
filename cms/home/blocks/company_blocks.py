from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

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
    lottie = basic_blocks.LottieBlock()
    text_content = basic_blocks.TextContentBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/featured_section_block.html'

from wagtail import blocks
from wagtail.images import blocks as i_blocks
# Project specific blocks
from base.blocks import basic_blocks

class TextContentBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Enter the section subtitle"
    )
    title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the section title"
    )
    body = blocks.TextBlock(
        required=True,
        help_text="Enter the section body text"
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/text_content_block.html'


class StatisticItemBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(
        required=False,
        help_text="Icon representing the statistic"
    )
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
    lottie_animation = basic_blocks.LottieAnimationBlock()
    text_content = TextContentBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/featured_section_block.html'

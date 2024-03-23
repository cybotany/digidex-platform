from base.blocks import basic_blocks

class StatisticItemBlock(basic_blocks.BaseStructBlock):
    icon = basic_blocks.BaseImageBlock()
    number = basic_blocks.BaseCharBlock(
        help_text="Statistic number"
    )
    description = basic_blocks.BaseCharBlock(
        help_text="Statistic description"
    )
    style = basic_blocks.BaseChoiceBlock(
        required=False,
        choices=[
            ('default', 'Default'),
            ('green', 'Green'),
        ],
        help_text="Statistic style",
        default='default')

    class Meta:
        icon = 'pick'
        template = 'base/blocks/apps/company/statistic_item_block.html'


class StatisticsGridBlock(basic_blocks.BaseStructBlock):
    statistics = basic_blocks.BaseListBlock(
        StatisticItemBlock(help_text="Add statistics")
    )

    class Meta:
        icon = 'grid'
        template = 'base/blocks/apps/company/statistics_grid_block.html'


class FeaturedSectionBlock(basic_blocks.BaseStructBlock):
    text_content = basic_blocks.BaseTextBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/company/featured_section_block.html'


class TeamMemberBlock(basic_blocks.BaseStructBlock):
    name = basic_blocks.BaseCharBlock(
        max_length=255
    )
    role = basic_blocks.BaseCharBlock(
        max_length=255
    )
    image = basic_blocks.BaseImageBlock()
    description = basic_blocks.BaseRichTextBlock(
        max_length=255
    )

class TestimonialBlock(basic_blocks.BaseStructBlock):
    quote = basic_blocks.BaseRichTextBlock(
        max_length=255
    )
    author = basic_blocks.BaseCharBlock(
        max_length=255
    )
    role = basic_blocks.BaseCharBlock(
        max_length=255,
        required=False
    )

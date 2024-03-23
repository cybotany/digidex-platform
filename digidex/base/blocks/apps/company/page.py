from base.blocks import basic


class StatisticItemBlock(basic.BaseStructBlock):
    icon = basic.BaseImageBlock()
    number = basic.BaseCharBlock(
        help_text="Statistic number"
    )
    description = basic.BaseCharBlock(
        help_text="Statistic description"
    )
    style = basic.BaseChoiceBlock(
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


class StatisticsGridBlock(basic.BaseStructBlock):
    statistics = basic.BaseListBlock(
        StatisticItemBlock(help_text="Add statistics")
    )

    class Meta:
        icon = 'grid'
        template = 'base/blocks/apps/company/statistics_grid_block.html'


class FeaturedSectionBlock(basic.BaseStructBlock):
    text_content = basic.BaseTextBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/company/featured_section_block.html'


class TeamMemberBlock(basic.BaseStructBlock):
    name = basic.BaseCharBlock(
        max_length=255
    )
    role = basic.BaseCharBlock(
        max_length=255
    )
    image = basic.BaseImageBlock()
    description = basic.BaseRichTextBlock(
        max_length=255
    )

class TestimonialBlock(basic.BaseStructBlock):
    quote = basic.BaseRichTextBlock(
        max_length=255
    )
    author = basic.BaseCharBlock(
        max_length=255
    )
    role = basic.BaseCharBlock(
        max_length=255,
        required=False
    )

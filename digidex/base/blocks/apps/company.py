from base.blocks import basics, components, layouts


class StatisticItemBlock(basics.BaseStructBlock):
    icon = basics.BaseImageBlock()
    number = basics.BaseCharBlock(
        help_text="Statistic number"
    )
    description = basics.BaseCharBlock(
        help_text="Statistic description"
    )
    style = basics.BaseChoiceBlock(
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


class StatisticsGridBlock(basics.BaseStructBlock):
    statistics = basics.BaseListBlock(
        StatisticItemBlock(help_text="Add statistics")
    )

    class Meta:
        icon = 'grid'
        template = 'base/blocks/apps/company/statistics_grid_block.html'


class FeaturedSectionBlock(basics.BaseStructBlock):
    text_content = basics.BaseTextBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/company/featured_section_block.html'


class TeamMemberBlock(basics.BaseStructBlock):
    name = basics.BaseCharBlock(
        max_length=255
    )
    role = basics.BaseCharBlock(
        max_length=255
    )
    image = basics.BaseImageBlock()
    description = basics.BaseRichTextBlock(
        max_length=255
    )

class TestimonialBlock(basics.BaseStructBlock):
    quote = basics.BaseRichTextBlock(
        max_length=255
    )
    author = basics.BaseCharBlock(
        max_length=255
    )
    role = basics.BaseCharBlock(
        max_length=255,
        required=False
    )

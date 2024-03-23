from base.blocks import basics as _blocks


class StatisticItemBlock(_blocks.BaseStructBlock):
    icon = _blocks.BaseImageBlock()
    number = _blocks.BaseCharBlock(
        help_text="Statistic number"
    )
    description = _blocks.BaseCharBlock(
        help_text="Statistic description"
    )
    style = _blocks.BaseChoiceBlock(
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


class StatisticsGridBlock(_blocks.BaseStructBlock):
    statistics = _blocks.BaseListBlock(
        StatisticItemBlock(help_text="Add statistics")
    )

    class Meta:
        icon = 'grid'
        template = 'base/blocks/apps/company/statistics_grid_block.html'


class FeaturedSectionBlock(_blocks.BaseStructBlock):
    text_content = _blocks.BaseTextBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/company/featured_section_block.html'


class TeamMemberBlock(_blocks.BaseStructBlock):
    name = _blocks.BaseCharBlock(
        max_length=255
    )
    role = _blocks.BaseCharBlock(
        max_length=255
    )
    image = _blocks.BaseImageBlock()
    description = _blocks.BaseRichTextBlock(
        max_length=255
    )

class TestimonialBlock(_blocks.BaseStructBlock):
    quote = _blocks.BaseRichTextBlock(
        max_length=255
    )
    author = _blocks.BaseCharBlock(
        max_length=255
    )
    role = _blocks.BaseCharBlock(
        max_length=255,
        required=False
    )


class CompanyContentBlock(_blocks.BaseContentBlock):
    pass

class CompanySectionBlock(_blocks.BaseSectionBlock):
    content = CompanyContentBlock()

    class Meta:
        icon = 'image'
        template = 'base/blocks/apps/company/section.html'

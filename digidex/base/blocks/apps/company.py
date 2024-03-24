from base.blocks import basics as _blocks
from base.blocks.apps import company as _company
from base.blocks.components import heading as _heading


class StatisticItem(_blocks.BaseStructBlock):
    icon = _blocks.BaseImageBlock()
    number = _blocks.BaseCharBlock(
        help_text="Statistic number"
    )
    description = _blocks.BaseCharBlock(
        help_text="Statistic description"
    )

    class Meta:
        icon = 'pick'
        template = 'base/blocks/apps/company/statistic_item_block.html'


class StatisticGrid(_blocks.BaseGridBlock):
    statistics = _blocks.BaseListBlock(
        StatisticItem(help_text="Add statistics")
    )

    class Meta:
        icon = 'grid'
        template = 'base/blocks/apps/company/statistics_grid_block.html'


class CompanyContent(_blocks.BaseContentBlock):
    #lottie = _blocks.BaseLottieBlock()
    block = _heading.HeadingBlock()
    grid = StatisticGrid()


class CompanySection(_blocks.BaseSectionBlock):
    content = CompanyContent()

    class Meta:
        icon = 'image'
        template = 'base/blocks/apps/company/section.html'


class FeaturedSectionBlock(_blocks.BaseStructBlock):
    text_content = _blocks.BaseTextBlock()
    statistics_grid = StatisticGrid()

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

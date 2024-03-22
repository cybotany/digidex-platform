from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class StatisticItemBlock(_bblocks.BaseStructBlock):
    icon = _bblocks.BaseImageBlock()
    number = _bblocks.BaseCharBlock(
        help_text="Statistic number"
    )
    description = _bblocks.BaseCharBlock(
        help_text="Statistic description"
    )
    style = _bblocks.BaseChoiceBlock(
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


class StatisticsGridBlock(_bblocks.BaseStructBlock):
    statistics = _bblocks.BaseListBlock(
        StatisticItemBlock(help_text="Add statistics")
    )

    class Meta:
        icon = 'grid'
        template = 'blocks/statistics_grid_block.html'


class FeaturedSectionBlock(_bblocks.BaseStructBlock):
    text_content = _bblocks.BaseTextBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/featured_section_block.html'

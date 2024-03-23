from base.blocks import basic_blocks as _bblocks,\
                        layout_blocks as _lblocks


class SolutionSectionBlock(_lblocks.SectionBlock):
    cards = _bblocks.BaseListBlock(
        SolutionCardBlock(),
        min_num=1,
        max_num=4,
        help_text="Add up to 4 solution cards. Each card will be displayed in a single row."
    )

    class Meta:
        icon = 'image'
        template = 'base/blocks/solutions/section.html'

from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class SolutionBlock(_bblocks.BaseStructBlock):
    icon = _bblocks.BaseImageBlock(
        required=True
    )
    title = _bblocks.BaseCharBlock(
        required=True,
        max_length=255
    )
    description = _bblocks.BaseTextBlock(
        required=True
    )
    link_url = _bblocks.BaseURLBlock(
        required=True
    )
    link_text = _bblocks.BaseCharBlock(
        default='Learn more',
        required=False
    )
    tag = _bblocks.BaseCharBlock(
        required=False,
        help_text='Optional tag like "Most popular" or "Best Value"'
    )

    class Meta:
        template = 'blocks/solution_block.html'


class ClientLogoBlock(_bblocks.BaseStructBlock):
    logo = _bblocks.BaseImageBlock(required=True)

    class Meta:
        template = 'blocks/client_logo_block.html'


class ReviewBlock(_bblocks.BaseStructBlock):
    review_text = _bblocks.BaseTextBlock(required=True)
    reviewer_name = _bblocks.BaseCharBlock(required=True, max_length=255)

    class Meta:
        template = 'blocks/review_block.html'



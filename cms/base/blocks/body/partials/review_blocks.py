# Project specific blocks
from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class StarRatingBlock(_bblocks.BaseStructBlock):
    stars = _bblocks.BaseIntegerBlock(
        min_value=1,
        max_value=5,
        default=5,
        help_text="Number of stars for the review"
    )

class ReviewBlock(_bblocks.BaseStructBlock):
    rating = StarRatingBlock()
    review_text = _bblocks.BaseTextBlock(
        required=True,
        help_text="The text of the review"
    )
    reviewer_name = _bblocks.BaseCharBlock(
        help_text="Name of the reviewer"
    )

    class Meta:
        icon = 'edit'
        template = 'blocks/review_block.html'


class ReviewsWrapperBlock(_bblocks.BaseStructBlock):
    reviews = _bblocks.BaseListBlock(
        ReviewBlock(help_text="Add reviews to the section")
    )

    class Meta:
        icon = 'group'
        template = 'blocks/reviews_wrapper_block.html'


class ReviewSectionBlock(_bblocks.BaseStructBlock):
    title = _cblocks.HeadingBlock()
    reviews = ReviewsWrapperBlock()
    button = _cblocks.ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/review_section_block.html'

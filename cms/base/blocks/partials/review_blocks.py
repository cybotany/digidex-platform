from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class StarRatingBlock(blocks.StructBlock):
    stars = blocks.IntegerBlock(
        min_value=1,
        max_value=5,
        default=5,
        help_text="Number of stars for the review"
    )

class ReviewBlock(blocks.StructBlock):
    rating = StarRatingBlock()
    review_text = blocks.TextBlock(
        required=True,
        help_text="The text of the review"
    )
    reviewer_name = basic_blocks.BaseCharBlock(
        help_text="Name of the reviewer"
    )

    class Meta:
        icon = 'edit'
        template = 'blocks/review_block.html'


class ReviewsWrapperBlock(blocks.StructBlock):
    reviews = blocks.ListBlock(
        ReviewBlock(help_text="Add reviews to the section")
    )

    class Meta:
        icon = 'group'
        template = 'blocks/reviews_wrapper_block.html'


class ReviewSectionBlock(blocks.StructBlock):
    title = basic_blocks.TextContentBlock()
    reviews = ReviewsWrapperBlock()
    button = basic_blocks.ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/review_section_block.html'

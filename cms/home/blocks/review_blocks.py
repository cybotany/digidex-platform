from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class SectionTitleBlock(basic_blocks.TextContentBlock):
    pass

    class Meta:
        icon = 'title'
        template = 'blocks/section_title_block.html'


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
    reviewer_name = blocks.CharBlock(
        required=True,
        max_length=255,
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

class ButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the button text"
    )
    button_link = blocks.URLBlock(
        required=True,
        help_text="Enter the URL the button will link to"
    )

    class Meta:
        icon = 'link'
        template = 'blocks/button_block.html'


class ReviewSectionBlock(blocks.StructBlock):
    title = SectionTitleBlock()
    reviews = ReviewsWrapperBlock()
    button = ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/review_section_block.html'

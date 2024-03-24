from base.blocks import basics as _blocks
                        

class ReviewCard(_blocks.BaseStructBlock):
    rating = _blocks.BaseIntegerBlock(
        min_value=0,
        max_value=5,
        default=5,
        help_text="Number of stars (0-5)"
    )
    feedback = _blocks.BaseTextBlock(
        required=True,
        help_text="The review text"
    )
    reviewer = _blocks.BaseCharBlock(
        required=True,
        help_text="Reviewer's name"
    )


class ReviewGrid(_blocks.BaseGridBlock):
    reviews = _blocks.BaseListBlock(
        ReviewCard(),
        help_text="Add reviews here",
    )


class ReviewHeading(_blocks.HeadingBlock):
    button = _blocks.ButtonBlock()


class ReviewContent(_blocks.BaseContentBlock):
    grid = ReviewGrid()
    block = ReviewHeading()


class ReviewSection(_blocks.BaseSectionBlock):
    content = ReviewContent()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/components/reviews.html'

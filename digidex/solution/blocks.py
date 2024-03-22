from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class AboutSectionBlock(_bblocks.BaseStructBlock):
    icon = _bblocks.BaseImageBlock(
        required=True
    )
    title = _bblocks.BaseCharBlock(
        required=True
    )
    text = _bblocks.BaseTextBlock(
        required=True
    )

    class Meta:
        template = 'blocks/about_section_block.html'


class QuoteBlock(_bblocks.BaseStructBlock):
    quote_text = _bblocks.BaseTextBlock(
        required=True
    )
    author_name = _bblocks.BaseCharBlock(
        required=True
    )
    author_role = _bblocks.BaseCharBlock(
        required=True
    )
    author_signature = _bblocks.BaseImageBlock(
        required=False
    )

    class Meta:
        template = 'blocks/quote_block.html'


class TeamMemberBlock(_bblocks.BaseStructBlock):
    image = _bblocks.BaseImageBlock(
        required=True
    )
    name = _bblocks.BaseCharBlock(
        required=True
    )
    role = _bblocks.BaseCharBlock(
        required=True
    )

    class Meta:
        template = 'blocks/team_member_block.html'


class ReviewBlock(_bblocks.BaseStructBlock):
    reviewer_name = _bblocks.BaseCharBlock(
        required=True
    )
    review_text = _bblocks.BaseTextBlock(
        required=True
    )
    star_rating = _bblocks.BaseIntegerBlock(
        required=True,
        min_value=1,
        max_value=5
    )

    class Meta:
        template = 'blocks/review_block.html'

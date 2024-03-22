from base.blocks import basic_blocks as _bblocks

class TeamMemberBlock(_bblocks.BaseStructBlock):
    name = _bblocks.BaseCharBlock(
        max_length=255
    )
    role = _bblocks.BaseCharBlock(
        max_length=255
    )
    image = _bblocks.BaseImageBlock()
    description = _bblocks.BaseTextBlock(
        max_length=255
    )

class TestimonialBlock(_bblocks.BaseStructBlock):
    quote = _bblocks.BaseTextBlock(
        max_length=255
    )
    author = _bblocks.BaseCharBlock(
        max_length=255
    )
    role = _bblocks.BaseCharBlock(
        max_length=255,
        required=False
    )

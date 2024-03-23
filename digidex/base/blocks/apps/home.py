from base.blocks import basic_blocks as _bblocks


class HeroSectionBlock(_bblocks.BaseStructBlock):
    heading = _bblocks.BaseCharBlock(
        required=True,
        max_length=255
    )
    sub_heading = _bblocks.BaseTextBlock(
        required=False
    )
    image = _bblocks.BaseImageBlock(
        required=False
    )
    cta = _bblocks.BaseStructBlock(
        [
            ("text", _bblocks.BaseCharBlock(required=True, max_length=255)),
            ("url", _bblocks.BaseURLBlock(required=True)),
        ]
    )

    class Meta:
        template = "blocks/hero_section.html"

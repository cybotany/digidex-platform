from base.blocks import basic_blocks


class HeroSectionBlock(basic_blocks.BaseStructBlock):
    heading = basic_blocks.BaseCharBlock(
        required=True,
        max_length=255
    )
    sub_heading = basic_blocks.BaseTextBlock(
        required=False
    )
    image = basic_blocks.BaseImageBlock(
        required=False
    )
    cta = basic_blocks.BaseStructBlock(
        [
            ("text", basic_blocks.BaseCharBlock(required=True, max_length=255)),
            ("url", basic_blocks.BaseURLBlock(required=True)),
        ]
    )

    class Meta:
        template = "blocks/hero_section.html"

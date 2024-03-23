from base.blocks import basic


class HeroContentBlock(basic.ContentBlock):
    subcontent = basic.BaseStreamBlock(
        #[
        #    ('solutions', SolutionGridBlock()),
        #    ('clients', SolutionClientsBlock()),
        #],
        min_num=1
    )


class HeroSectionBlock(basic.BaseStructBlock):
    heading = basic.BaseCharBlock(
        required=True,
        max_length=255
    )
    sub_heading = basic.BaseTextBlock(
        required=False
    )
    image = basic.BaseImageBlock(
        required=False
    )
    cta = basic.BaseStructBlock(
        [
            ("text", basic.BaseCharBlock(required=True, max_length=255)),
            ("url", basic.BaseURLBlock(required=True)),
        ]
    )

    class Meta:
        template = "blocks/hero_section.html"

from base.blocks import basics, components, layouts


class HeroContentBlock(layouts.ContentBlock):
    pass


class HeroSectionBlock(layouts.SectionBlock):
    heading = basics.BaseCharBlock(
        required=True,
        max_length=255
    )
    sub_heading = basics.BaseTextBlock(
        required=False
    )
    image = basics.BaseImageBlock(
        required=False
    )
    cta = basics.BaseStructBlock(
        [
            ("text", basics.BaseCharBlock(required=True, max_length=255)),
            ("url", basics.BaseURLBlock(required=True)),
        ]
    )

    class Meta:
        template = "blocks/hero_section.html"

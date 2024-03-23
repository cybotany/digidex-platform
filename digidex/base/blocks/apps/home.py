from base.blocks import basics, components, layouts


class HeroBlock(layouts.BaseBlock):
    heading = basics.BaseCharBlock(
        required=True,
        max_length=255
    )
    text = basics.BaseTextBlock(
        required=True
    )
    primary_button = components.ButtonBlock(
        required=True
    )
    secondary_button = components.ButtonBlock(
        required=False
    )


class HeroContent(layouts.ContentBlock):
    pass


class HeroSection(layouts.SectionBlock):
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

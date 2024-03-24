from base.blocks import basics as _blocks


class HeadingBlock(_blocks.BaseBlock):
    title = _blocks.BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    subtitle = _blocks.BaseCharBlock(
        required=False,
        help_text="Enter the heading subtitle"
    )
    text = _blocks.BaseTextBlock(
        required=False,
        help_text="Enter the heading text"
    )

    class Meta:
        icon = "placeholder"
        template = "base/blocks/components/heading.html"
        label = "Section Heading"


class HeadingSectionContent(_blocks.BaseContentBlock):
    title = _blocks.BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    text = _blocks.BaseTextBlock(
        required=True,
        help_text="Enter the heading text"
    )


class HeadingSection(_blocks.BaseSectionBlock):
    content = HeadingSectionContent()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/app/heading.html"
        label = "Page Heading"

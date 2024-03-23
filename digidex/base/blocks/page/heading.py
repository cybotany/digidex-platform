from base.blocks import basics as _blocks


class HeadingBlock(_blocks.BaseBlock):
    title = _blocks.BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    text = _blocks.BaseTextBlock(
        required=True,
        help_text="Enter the heading text"
    )


class HeadingContentBlock(_blocks.BaseContentBlock):
    pass


class HeadingSectionBlock(_blocks.BaseSectionBlock):
    content = HeadingContentBlock()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/apps/navigation/heading.html"
        label = "Page Header"

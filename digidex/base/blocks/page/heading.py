from base.blocks import basic


class HeadingBlock(basic.BaseBlock):
    title = basic.BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    text = basic.BaseTextBlock(
        required=True,
        help_text="Enter the heading text"
    )


class HeadingContent(basic.ContentBlock):
    block = HeadingBlock()


class HeadingSection(basic.SectionBlock):
    content = HeadingContent()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/apps/navigation/heading.html"
        label = "Page Header"

from base.blocks import basics, components, layouts


class HeadingBlock(layouts.BaseBlock):
    title = basics.BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    text = basics.BaseTextBlock(
        required=True,
        help_text="Enter the heading text"
    )


class HeadingContent(layouts.ContentBlock):
    block = HeadingBlock()


class HeadingSection(layouts.SectionBlock):
    content = HeadingContent()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/apps/navigation/heading.html"
        label = "Page Header"

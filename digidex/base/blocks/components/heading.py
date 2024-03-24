from base.blocks import basics as _blocks


class SectionHeading(_blocks.BaseBlock):
    title = _blocks.BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    subtitle = _blocks.BaseTextBlock(
        required=False,
        help_text="Enter the heading subtitle"
    )
    centered = _blocks.BaseBooleanBlock(
        required=False,
        default=False,
        help_text="Should the heading be centered?"
    )

    class Meta:
        icon = "placeholder"
        template = "base/blocks/section/heading.html"
        label = "Section Heading"



class PageHeadingContent(_blocks.BaseContentBlock):
    title = _blocks.BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    text = _blocks.BaseTextBlock(
        required=True,
        help_text="Enter the heading text"
    )


class PageHeading(_blocks.BaseSectionBlock):
    content = PageHeadingContent()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/page/heading.html"
        label = "Page Heading"

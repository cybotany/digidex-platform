from base.blocks import basics as _blocks


class SolutionTagBlock(_blocks.BaseStructBlock):
    text = _blocks.BaseCharBlock(
        required=True,
        help_text="Enter the text for the tag (e.g., 'Most popular')."
    )
    color = _blocks.BaseChoiceBlock(
        choices=[
            ('yellow', 'Yellow'),
            ('blue', 'Blue'),
        ],
        required=True,
        help_text="Select the color of the tag."
    )


class SolutionCardContentBlock(_blocks.BaseStructBlock):
    image = _blocks.BaseImageBlock(
        required=True,
        help_text="Select an image for the solution card."
    )
    heading = _blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter the heading for the solution card."
    )
    paragraph = _blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a descriptive paragraph for the solution."
    )


class SolutionCardIconBlock(_blocks.BaseStructBlock):
    icon = _blocks.BaseImageBlock(
        required=True,
        help_text="Select an icon image to represent the link."
    )
    text = _blocks.BaseCharBlock(
        required=True,
        help_text="Enter the text for the link."
    )
    page = _blocks.BasePageBlock(
        required=False,
        help_text="Select the destination page for the link."
    )
    target = _blocks.BaseChoiceBlock(
        choices=[
            ('_self', 'Open in the same window'),
            ('_blank', 'Open in a new window')
        ],
        required=True,
        help_text="Choose where the link should open."
    )


class SolutionCardBlock(_blocks.BaseBlock):
    tag = SolutionTagBlock(
        required=False,
        help_text="Optionally add a tag to the card, such as 'Most popular' or 'New'."
    )
    content = SolutionCardContentBlock(
        help_text="Add the main content for the card."
    )
    button = SolutionCardIconBlock(
        required=True,
        help_text="Define an icon with a link for additional details or actions."
    )


class SolutionGridBlock(_blocks.BaseGridBlock):
    items = _blocks.BaseListBlock(
        SolutionCardBlock(),
        min_num=1,
        max_num=4,
        help_text="Add up to 4 solution cards. Each card will be displayed in a single row."
    )

    class Meta:
        icon = 'image'
        template = 'base/blocks/solution/grid.html'


class ClientLogoBlock(_blocks.BaseStructBlock):
    image = _blocks.BaseImageBlock(
        required=True,
        help_text="Select a client logo image."
    )
    alt_text = _blocks.BaseCharBlock(
        required=False,
        max_length=255,
        help_text="Enter an alternative text for the image."
    )

    class Meta:
        icon = 'image'


class SolutionClientsBlock(_blocks.BaseBlock):
    subtitle = _blocks.BaseCharBlock(
        required=False,
        max_length=255,
        help_text="Enter a subtitle for the clients section."
    )
    logos = _blocks.BaseListBlock(
        ClientLogoBlock(),
        help_text="Add client logos."
    )

    class Meta:
        icon = 'group'
        template = 'base/blocks/apps/solution/clients.html'


class SolutionContentBlock(_blocks.BaseContentBlock):
    pass


class SolutionSection(_blocks.BaseSectionBlock):
    content = SolutionContentBlock()

    class Meta:
        icon = 'image'
        template = 'base/blocks/apps/solution/section.html'

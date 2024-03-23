from base.blocks import basic_blocks,\
                        composite_blocks

class SolutionTagBlock(composite_blocks.TagBlock):
    text = basic_blocks.BaseCharBlock(
        required=True,
        help_text="Enter the text for the tag (e.g., 'Most popular')."
    )
    color = basic_blocks.BaseChoiceBlock(
        choices=[
            ('yellow', 'Yellow'),
            ('blue', 'Blue'),
        ],
        required=True,
        help_text="Select the color of the tag."
    )


class SolutionCardContentBlock(composite_blocks.IconBlock):
    image = basic_blocks.BaseImageBlock(
        required=True,
        help_text="Select an image for the solution card."
    )
    heading = basic_blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter the heading for the solution card."
    )
    paragraph = basic_blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a descriptive paragraph for the solution."
    )


class SolutionCardIconBlock(composite_blocks.IconBlock):
    icon = basic_blocks.BaseImageBlock(
        required=True,
        help_text="Select an icon image to represent the link."
    )
    text = basic_blocks.BaseCharBlock(
        required=True,
        help_text="Enter the text for the link."
    )
    page = basic_blocks.BasePageBlock(
        required=False,
        help_text="Select the destination page for the link."
    )
    target = basic_blocks.BaseChoiceBlock(
        choices=[
            ('_self', 'Open in the same window'),
            ('_blank', 'Open in a new window')
        ],
        required=True,
        help_text="Choose where the link should open."
    )


class SolutionCardBlock(basic_blocks.BaseBlock):
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


class SolutionGridBlock(basic_blocks.GridBlock):
    items = basic_blocks.BaseListBlock(
        SolutionCardBlock(),
        min_num=1,
        max_num=4,
        help_text="Add up to 4 solution cards. Each card will be displayed in a single row."
    )

    class Meta:
        icon = 'image'
        template = 'base/blocks/solution/grid.html'


class ClientLogoBlock(basic_blocks.BaseStructBlock):
    image = basic_blocks.BaseImageBlock(
        required=True,
        help_text="Select a client logo image."
    )
    alt_text = basic_blocks.BaseCharBlock(
        required=False,
        max_length=255,
        help_text="Enter an alternative text for the image."
    )

    class Meta:
        icon = 'image'


class SolutionClientsBlock(basic_blocks.BaseBlock):
    subtitle = basic_blocks.BaseCharBlock(
        required=False,
        max_length=255,
        help_text="Enter a subtitle for the clients section."
    )
    logos = basic_blocks.BaseListBlock(
        ClientLogoBlock(),
        help_text="Add client logos."
    )

    class Meta:
        icon = 'group'
        template = 'base/blocks/apps/solution/clients.html'


class SolutionContentBlock(basic_blocks.ContentBlock):
    subcontent = basic_blocks.BaseStreamBlock(
        [
            ('solutions', SolutionGridBlock()),
            ('clients', SolutionClientsBlock()),
        ],
        max_num=1
    )

class SolutionSectionBlock(basic_blocks.SectionBlock):
    content = SolutionContentBlock()

    class Meta:
        icon = 'image'
        template = 'base/blocks/apps/solution/section.html'

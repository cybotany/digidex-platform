from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class SolutionTagBlock(_cblocks.TagBlock):
    text = _bblocks.BaseCharBlock(
        required=True,
        help_text="Enter the text for the tag (e.g., 'Most popular')."
    )
    color = _bblocks.BaseChoiceBlock(
        choices=[
            ('yellow', 'Yellow'),
            ('blue', 'Blue'),
        ],
        required=True,
        help_text="Select the color of the tag."
    )


class SolutionCardContentBlock(_cblocks.IconBlock):
    image = _bblocks.BaseImageBlock(
        required=True,
        help_text="Select an image for the solution card."
    )
    heading = _bblocks.BaseRichTextBlock(
        required=True,
        help_text="Enter the heading for the solution card."
    )
    paragraph = _bblocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a descriptive paragraph for the solution."
    )


class SolutionCardIconBlock(_cblocks.IconBlock):
    icon = _bblocks.BaseImageBlock(
        required=True,
        help_text="Select an icon image to represent the link."
    )
    text = _bblocks.BaseCharBlock(
        required=True,
        help_text="Enter the text for the link."
    )
    page = _bblocks.BasePageBlock(
        required=False,
        help_text="Select the destination page for the link."
    )
    target = _bblocks.BaseChoiceBlock(
        choices=[
            ('_self', 'Open in the same window'),
            ('_blank', 'Open in a new window')
        ],
        required=True,
        help_text="Choose where the link should open."
    )


class SolutionCardBlock(_lblocks.BaseBlock):
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


class SolutionGridBlock(_lblocks.GridBlock):
    items = _bblocks.BaseListBlock(
        SolutionCardBlock(),
        min_num=1,
        max_num=4,
        help_text="Add up to 4 solution cards. Each card will be displayed in a single row."
    )

    class Meta:
        icon = 'image'
        template = 'base/blocks/solution/grid.html'


class ClientLogoBlock(_bblocks.BaseStructBlock):
    image = _bblocks.BaseImageBlock(
        required=True,
        help_text="Select a client logo image."
    )
    alt_text = _bblocks.BaseCharBlock(
        required=False,
        max_length=255,
        help_text="Enter an alternative text for the image."
    )

    class Meta:
        icon = 'image'


class SolutionClientsBlock(_lblocks.BaseBlock):
    subtitle = _bblocks.BaseCharBlock(
        required=False,
        max_length=255,
        help_text="Enter a subtitle for the clients section."
    )
    logos = _bblocks.BaseListBlock(
        ClientLogoBlock(),
        help_text="Add client logos."
    )

    class Meta:
        icon = 'group'
        template = 'base/blocks/apps/solution/clients.html'


class SolutionContentBlock(_lblocks.ContentBlock):
    subcontent = _bblocks.BaseStreamBlock(
        [
            ('solutions', SolutionGridBlock()),
            ('clients', SolutionClientsBlock()),
        ],
        max_num=1
    )

class SolutionSectionBlock(_lblocks.SectionBlock):
    content = SolutionContentBlock()

    class Meta:
        icon = 'image'
        template = 'base/blocks/apps/solution/section.html'

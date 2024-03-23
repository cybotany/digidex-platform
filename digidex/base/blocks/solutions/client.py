from base.blocks import basic_blocks as _bblocks,\
                        layout_blocks as _lblocks


class ClientLogoBlock(_bblocks.BaseStructBlock):
    """
    A block representing a single client logo.
    """
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
    """
    A block representing a section of client logos with a subtitle.
    """
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
        template = 'base/blocks/solutions/clients.html'

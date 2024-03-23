from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks


class ClientLogoBlock(blocks.StructBlock):
    """
    A block representing a single client logo.
    """
    image = ImageChooserBlock(
        required=True,
        help_text="Select a client logo image."
    )
    alt_text = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Enter an alternative text for the image."
    )

    class Meta:
        icon = 'image'


class SolutionClientsBlock(blocks.StructBlock):
    """
    A block representing a section of client logos with a subtitle.
    """
    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Enter a subtitle for the clients section."
    )
    logos = blocks.ListBlock(
        ClientLogoBlock(),
        help_text="Add client logos."
    )

    class Meta:
        icon = 'group'
        template = 'base/blocks/solutions/clients.html'

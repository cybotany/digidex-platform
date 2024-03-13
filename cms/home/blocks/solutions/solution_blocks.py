# Project specific blocks
from cms.base.blocks import layout_blocks as _lblocks
from cms.base.blocks import basic_blocks as _bblocks, composite_blocks as _cblocks

class SolutionBlock(_lblocks.SectionBlock):
    icon = _bblocks.BaseImageBlock()
    content = _cblocks.TextContentBlock()
    link = blocks.PageChooserBlock(
        required=True,
        help_text="Select a page for 'Learn more' link"
    )
    tag = _bblocks.BaseCharBlock(
        required=False,
        choices=[
            ('most_popular', 'Most popular'),
            ('best_value', 'Best Value')
        ], 
        help_text="Tag for the solution (optional)"
    )

    class Meta:
        icon = 'solution'
        template = 'blocks/solution_block.html'


class SolutionsGridBlock(_lblocks.GridBlock):
    solutions = _bblocks.BaseListBlock(
        SolutionBlock(help_text="Add solutions to the grid")
    )

    class Meta:
        icon = 'grid'
        template = 'blocks/solutions_grid_block.html'


class ClientLogoBlock(blocks.StructBlock):
    logo = _bblocks.BaseImageBlock(
        help_text="Select a client logo"
    )

    class Meta:
        icon = 'image'
        template = 'blocks/client_logo_block.html'


class ClientsGridBlock(blocks.StructBlock):
    title = _cblocks.HeadingBlock()
    logos = _bblocks.BaseListBlock(
        ClientLogoBlock(help_text="Add client logos")
    )

    class Meta:
        icon = 'group'
        template = 'blocks/clients_grid_block.html'

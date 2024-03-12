from wagtail import blocks
# Project specific blocks
from cms.base.blocks import basic_blocks

class SolutionBlock(blocks.StructBlock):
    icon = basic_blocks.BaseImageBlock()
    content = basic_blocks.TextContentBlock()
    link = blocks.PageChooserBlock(
        required=True,
        help_text="Select a page for 'Learn more' link"
    )
    tag = blocks.CharBlock(
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


class SolutionsGridBlock(blocks.StructBlock):
    solutions = blocks.ListBlock(
        SolutionBlock(help_text="Add solutions to the grid")
    )

    class Meta:
        icon = 'grid'
        template = 'blocks/solutions_grid_block.html'


class ClientLogoBlock(blocks.StructBlock):
    logo = basic_blocks.BaseImageBlock(
        help_text="Select a client logo"
    )

    class Meta:
        icon = 'image'
        template = 'blocks/client_logo_block.html'


class ClientsGridBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    logos = blocks.ListBlock(
        ClientLogoBlock(help_text="Add client logos")
    )

    class Meta:
        icon = 'group'
        template = 'blocks/clients_grid_block.html'

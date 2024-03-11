from wagtail import blocks
from wagtail.images import blocks as i_blocks

class SolutionBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(required=True, help_text="Select an icon for the solution")
    title = blocks.CharBlock(required=True, max_length=255, help_text="Enter the solution title")
    description = blocks.TextBlock(required=True, help_text="Enter the solution description")
    link_url = blocks.URLBlock(required=True, help_text="Enter the URL for 'Learn more' link")
    tag = blocks.CharBlock(required=False, max_length=255, help_text="Tag for the solution (optional)")

    class Meta:
        icon = 'solution'
        template = 'blocks/solution_block.html'


class SolutionsGridBlock(blocks.StructBlock):
    solutions = blocks.ListBlock(SolutionBlock(help_text="Add solutions to the grid"))

    class Meta:
        icon = 'grid'
        template = 'blocks/solutions_grid_block.html'


class ClientLogoBlock(blocks.StructBlock):
    logo = i_blocks.ImageChooserBlock(required=True, help_text="Select a client logo")

    class Meta:
        icon = 'image'
        template = 'blocks/client_logo_block.html'


class ClientsGridBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255, help_text="Title for the clients section")
    logos = blocks.ListBlock(ClientLogoBlock(help_text="Add client logos"))

    class Meta:
        icon = 'group'
        template = 'blocks/clients_grid_block.html'

from wagtail.core import blocks as core_blocks
# Project specific imports
from base import blocks

class HowItWorksBlock(core_blocks.StructBlock):
    subtitle = core_blocks.CharBlock(required=True, max_length=100)
    heading = core_blocks.CharBlock(required=True, max_length=200)
    paragraph = core_blocks.TextBlock(required=True)
    steps = core_blocks.ListBlock(blocks.StepBlock())

    class Meta:
        template = 'blocks/how_it_works_block.html'
        icon = 'snippet'

from wagtail import blocks
from wagtail.images import blocks as img_blocks

class LearnMoreBlock(blocks.StructBlock):
    link = blocks.PageChooserBlock(
        required=True
    )
    text = blocks.CharBlock(
        default="Learn more",
        required=True
    )
    image = img_blocks.ImageChooserBlock(
        required=True
    )

    class Meta:
        template = 'base/blocks/buttons/learn_more_block.html'


class SolutionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=True
    )
    paragraph = blocks.RichTextBlock(
        required=False
    )
    link = LearnMoreBlock()

    class Meta:
        icon = "image"
        template = "solutions/blocks/solution_block.html"

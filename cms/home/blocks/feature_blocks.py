from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class FeatureItemBlock(blocks.StructBlock):
    icon = basic_blocks.BaseIconBlock()
    content = basic_blocks.TextContentBlock()

    class Meta:
        icon = 'pick'
        template = 'blocks/feature_item_block.html'


class FeaturesGridBlock(blocks.StructBlock):
    features = blocks.ListBlock(
        FeatureItemBlock(help_text="Add feature items to display in a grid")
    )

    class Meta:
        icon = 'grid'
        template = 'blocks/features_grid_block.html'


class SectionHeadingBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()

    class Meta:
        icon = 'title'
        template = 'blocks/section_heading_block.html'


class HostingFeaturesSectionBlock(blocks.StructBlock):
    heading = SectionHeadingBlock()
    features_grid = FeaturesGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/hosting_features_section_block.html'

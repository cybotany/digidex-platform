from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class FeatureItemBlock(blocks.StructBlock):
    icon = basic_blocks.BaseURLBlock()
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


class SectionHeadingBlock(basic_blocks.BaseTitleBlock):
    pass
    class Meta:
        icon = 'title'
        template = 'blocks/section_heading_block.html'


class HostingFeaturesSectionBlock(SectionHeadingBlock):
    features_grid = FeaturesGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/hosting_features_section_block.html'

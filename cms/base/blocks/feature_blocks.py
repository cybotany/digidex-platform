from wagtail import blocks
from wagtail.images import blocks as i_blocks

class FeatureItemBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(
        required=True,
        help_text="Select an icon for the feature"
    )
    title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the feature title"
    )
    description = blocks.TextBlock(
        required=True,
        help_text="Enter the feature description"
    )

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
    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Enter the section subtitle"
    )
    title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the section title"
    )

    class Meta:
        icon = 'title'
        template = 'blocks/section_heading_block.html'


class HostingFeaturesSectionBlock(blocks.StructBlock):
    heading = SectionHeadingBlock()
    features_grid = FeaturesGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/hosting_features_section_block.html'

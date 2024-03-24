from base.blocks import basics as _blocks
from base.blocks.components import heading as _heading
                        

class FeatureBlock(_blocks.BaseStructBlock):
    icon = _blocks.BaseImageBlock(required=True, help_text="Feature icon")
    heading = _blocks.BaseCharBlock(required=True, help_text="Feature heading")
    text = _blocks.BaseTextBlock(required=True, help_text="Feature description")

    class Meta:
        template = "blocks/feature_block.html"
        icon = "placeholder"
        label = "Feature"


class FeatureContent(_blocks.BaseContentBlock):
    block = _heading.HeadingBlock()


class FeatureSection(_blocks.BaseSectionBlock):
    content = FeatureContent()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/components/feature_section.html'

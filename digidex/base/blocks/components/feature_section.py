from base.blocks import basics as _blocks
                        

class FeatureBlock(_blocks.BaseStructBlock):
    icon = _blocks.BaseImageBlock(
        required=True,
        help_text="Feature icon"
    )
    heading = _blocks.BaseCharBlock(
        required=True,
        help_text="Feature heading"
    )
    text = _blocks.BaseTextBlock(
        required=True,
        help_text="Feature description"
    )

    class Meta:
        icon = "placeholder"
        label = "Feature"


class FeatureGrid(_blocks.BaseGridBlock):
    features = _blocks.BaseStreamBlock(
        [
            ('feature', FeatureBlock())
        ],
        max_num=6,
        help_text="Add features here",
    )


class FeatureContent(_blocks.BaseContentBlock):
    block = _blocks.HeadingBlock()
    grid = FeatureGrid()


class FeatureSection(_blocks.BaseSectionBlock):
    content = FeatureContent()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/components/feature_section.html'

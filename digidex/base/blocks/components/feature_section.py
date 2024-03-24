from base.blocks import basics as _blocks
                        

class FeatureContent(_blocks.BaseContentBlock):
    pass


class FeatureSection(_blocks.BaseSectionBlock):
    content = FeatureContent()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/components/feature_section.html'

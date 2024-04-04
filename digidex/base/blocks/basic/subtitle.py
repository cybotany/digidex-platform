from wagtail import blocks

class _Subtitle(blocks.CharBlock):
    pass

class SubtitleBlock(blocks.CharBlock):
    text = _Subtitle()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/basic/subtitle_block.html"

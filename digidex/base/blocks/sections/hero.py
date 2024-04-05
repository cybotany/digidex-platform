from base.blocks import basic as _bblocks,\
                        lottie as _lblocks


class HeroSection(_bblocks._SectionBlock):
    heading = _bblocks._HeadingBlock()
    introduction = _bblocks._ParagraphBlock()

    lottie = _lblocks.Lottie()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/page/hero_section.html"

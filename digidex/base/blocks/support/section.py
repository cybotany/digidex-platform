from base.blocks import layout_blocks as _lblocks
from base.blocks.support import heading, lottie



class ContactSectionBlock(_lblocks.SectionBlock):
    title = heading.ContactHeadingBlock()
    lottie = lottie.ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'

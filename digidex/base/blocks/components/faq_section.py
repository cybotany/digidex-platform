from base.blocks import basics as _blocks
                        

class FAQBlock(_blocks.BaseBlock):
    question = _blocks.BaseCharBlock(
        required=True,
        help_text="FAQ question"
    )
    answer = _blocks.BaseTextBlock(
        required=True,
        help_text="FAQ answer"
    )

    class Meta:
        icon = "question"
        label = "FAQ Item"


class FAQGrid(_blocks.BaseGridBlock):
    faqs = _blocks.BaseListBlock(
        FAQBlock(),
        help_text="Add FAQ items here"
    )


class FAQContent(_blocks.BaseContentBlock):
    block = _blocks.HeadingBlock()
    grid = FAQGrid()


class FAQSection(_blocks.BaseSectionBlock):
    content = FAQContent()

    class Meta:
        icon = 'help'
        label = "FAQ Section"
        template = 'base/blocks/components/faq_section.html'

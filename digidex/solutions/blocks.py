from base import blocks as _blocks

class SolutionBlock(_blocks.ContentBlock):
    pass


class LargeSolutionBlock(_blocks.ContentBlock):
    value_propositions = _blocks.BaseListBlock()


class SolutionsStreamBlock(_blocks.BaseStreamBlock):
    solution = SolutionBlock(
        help_text="Solution sections"
    )


class FeaturesStreamBlock(_blocks.BaseStreamBlock):
    feature = _blocks.ContentBlock(
        help_text="Feature sections"
    )

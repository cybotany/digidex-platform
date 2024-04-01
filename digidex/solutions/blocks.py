from base import blocks as _blocks

class SolutionBlock(_blocks.ContentBlock):
    page = _blocks.BasePageBlock(
        required=False,
        help_text="Link to a page"
    )

class LargeSolutionBlock(_blocks.ContentBlock):
    value_propositions = _blocks.BaseListBlock(
        _blocks.BaseItemBlock(),
        help_text="List of value propositions for the solution"
    )

class SolutionsStreamBlock(_blocks.BaseStreamBlock):
    solution = SolutionBlock()

class FeatureBlock(_blocks.ContentBlock):
    pass

class FeaturesStreamBlock(_blocks.BaseStreamBlock):
    feature = FeatureBlock()

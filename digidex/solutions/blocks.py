from base import blocks as _blocks

class SolutionBlock(_blocks.ContentBlock):
    linked_page = _blocks.PageBodyBlock(
        required=False,
        help_text="Link to a page"
    )


class LargeSolutionBlock(_blocks.ContentBlock):
    value_propositions = _blocks.BaseListBlock(
        child_block=_blocks.BaseListItemBlock(),
        help_text="List of value propositions for the solution"
    )


class SolutionsStreamBlock(_blocks.BaseStreamBlock):
    solution = SolutionBlock(
        help_text="Solution sections"
    )


class FeaturesStreamBlock(_blocks.BaseStreamBlock):
    feature = _blocks.ContentBlock(
        help_text="Feature sections"
    )

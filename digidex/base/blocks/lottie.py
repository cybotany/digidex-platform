from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock

class LottieAnimationBlock(blocks.StructBlock):
    animation_file = DocumentChooserBlock(required=True, help_text="Select the Lottie JSON file.")
    loop = blocks.BooleanBlock(required=False, help_text="Enable to loop the animation.")
    autoplay = blocks.BooleanBlock(required=False, default=True, help_text="Enable to autoplay the animation.")
    animation_duration = blocks.FloatBlock(required=False, help_text="Duration of the animation in seconds.", default=0)
    animation_direction = blocks.ChoiceBlock(choices=[(1, "Normal"), (-1, "Reverse")], default=1, help_text="Play animation in normal or reverse direction.")
    renderer = blocks.ChoiceBlock(choices=[("svg", "SVG"), ("canvas", "Canvas"), ("html", "HTML")], default="svg", help_text="Rendering mode of the animation.")

    class Meta:
        icon = "media"
        template = "blocks/lottie_animation_block.html"

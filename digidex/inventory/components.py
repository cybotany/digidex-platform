from dataclasses import dataclass, asdict
from laces.components import Component

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    IconComponent,
    TextComponent
)
from inventory.models import InventoryIndex


@dataclass
class Dashboard(Component):
    template_name: str = 'inventory/components/dashboard.html'

    panels: list = None

    @classmethod
    def from_user(cls, user):
        inventory = InventoryIndex.objects.get(owner=user)
        categories = inventory.get_children()

        if not categories.exists():
            pass

        heading_section = SectionComponent(
            children=[
                BlockComponent(
                    children = [
                        HeadingComponent(
                            text=inventory.__str__(),
                            size=1,
                            style='heading-top'
                        ),
                        BlockComponent()
                    ],
                    style='block-top'
                )
            ],
            style='section-top'
        )
        
        return cls(
            panels=[heading_section]
        )

    def get_context_data(self, parent_context=None):
        return asdict(self)

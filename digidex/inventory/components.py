from dataclasses import dataclass, asdict
from laces.components import Component

from inventory.models import UserProfile


@dataclass
class Categories(Component):
    template_name = 'inventory/components/categories.html'

    name: str
    description: str

    @classmethod
    def from_user(cls, user):
        user_profile = UserProfile.objects.select_related('inventory').get(user__id=user.id)
        user_inventory = user_profile.inventory
        
        children = user_inventory.get_children()
        if children.exists():
            name = user_inventory.name
            description = user_inventory.description
            
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            profile_url=profile_url,
            profile_image_url=user.profile.image.url,
        )

    def get_context_data(self, parent_context=None):
        return asdict(self)
from wagtail.snippets.models import register_snippet

from inventory.models import Inventory, Category, Item, Link

register_snippet(Inventory)
register_snippet(Category)
register_snippet(Item)
register_snippet(Link)

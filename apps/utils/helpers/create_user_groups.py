from apps.groups.models import Group
from apps.utils.constants import MAX_GROUP

def create_user_groups(user, existing_groups_count=0):
    """
    Create default groups for a user up to the MAX_GROUP limit.
    """
    for i in range(existing_groups_count + 1, MAX_GROUP + 1):
        Group.objects.get_or_create(user=user, name=f'Group {i}', position=i)

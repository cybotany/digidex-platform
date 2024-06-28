from wagtail.models import Collection

def get_root_collection():
    root_collection = Collection.get_first_root_node()
    if not root_collection:
        root_collection = Collection.add_root(name='Root')
    return root_collection

def get_user_collection():
    root_collection = get_root_collection()
    try:
        user_collection = Collection.objects.get(name='Users')
    except Collection.DoesNotExist:
        user_collection = root_collection.add_child(name='Users')
    return user_collection

def create_trainer_collection(user):
    user_collection = get_user_collection()
    try:
        trainer_collection = Collection.objects.get(name=user.username)
    except Collection.DoesNotExist:
        trainer_collection = user_collection.add_child(name=user.username)
    return trainer_collection

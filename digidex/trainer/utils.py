from home.utils import get_user_collection

def create_trainer_collection(user):
    user_collection = get_user_collection()
    trainer_collection = user_collection.add_child(name=user.username)
    return trainer_collection

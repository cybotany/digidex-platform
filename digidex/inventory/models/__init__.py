from .pet import Pet
from .plant import Plant
from .grouping import Grouping
from .profile import Profile, profile_avatar_directory_path

MODEL_MAP = {
    'pet': Pet,
    'plant': Plant,
}
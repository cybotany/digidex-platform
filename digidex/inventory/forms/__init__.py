from .profile import ProfileForm
from .grouping import GroupingForm
from .pet import PetForm
from .plant import PlantForm

FORM_MAP = {
    'pet': PetForm,
    'plant': PlantForm,
}
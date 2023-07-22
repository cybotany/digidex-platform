ACTIVITY_STATUS = [
    ('register', 'Registered'),
    ('update', 'Updated'),
    ('delete', 'Deleted'),
]

ACTIVITY_TYPE = [
    ('plant', 'Plant'),
    ('growing_fertilizer', 'Growing Fertilizer'),
    ('growing_label', 'Growing Label'),
    ('growing_medium', 'Growing Medium'),
    ('growing_component', 'Growing Component'),
    ('greenhouse', 'Greenhouse'),
    ('growth chamber', 'Growth Chamber'),
    ('tissue culture chamber', 'Tissue Culture Chamber'),
]

MEASUREMENT_CHOICES = [
    ('in', 'Inches'),
    ('cm', 'Centimeters'),
]

SENSOR_TYPE_CHOICES = [
    ('temp', 'Temperature'),
    ('humidity', 'Humidity'),
    ('light', 'Light'),
    ('voc', 'Air Quality'),
]

INSTRUMENT_TYPE_CHOICES = [
    ('camera', 'Camera'),
    ('light', 'Light'),
    ('fan', 'Fan'),
]

COMMON_LABELS = [
    'Living Room',
    'Kitchen',
    'Balcony',
    'Patio',
    'Garden',
    'Bedroom',
    'Bathroom',
    'Office'
]

GROWING_METHODS = [
    ('Traditional', 'Traditional'),
    ('Hydroponics', 'Hydroponics'),
]

GROWING_MEDIUM_COMPONENT = [
    ('Soil', 'Soil'),
    ('Coco Coir', 'Coco Coir'),
    ('Pine Coir', 'Pine Coir'),
    ('Rockwool', 'Rockwool'),
    ('LECA', 'LECA'),
    ('Perlite', 'Perlite'),
    ('Vermiculite', 'Vermiculite'),
    ('Calcined Clay', 'Calcined Clay'),
    ('Montmorillonite Clay', 'Montmorillonite Clay'),
    ('Sphagnum Moss', 'Sphagnum Moss'),
    ('Peat Moss', 'Peat Moss'),
]

INTERESTS_CHOICES = [
    ('gardening', 'Gardening'),
    ('hydroponics', 'Hydroponics'),
    ('botany', 'Botany'),
    ('farming', 'Farming')
]

EXPERIENCE_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
    ('expert', 'Expert')
]

MESSAGE_TYPES = [
    ('H', 'Human'),
    ('A', 'AI'),
    ('G', 'Agent'),
]

CHAT_TEMPLATE = """
    This is a friendly conversation between a human and an AI.
    The AI is talkative and provides lots of specific details from its context.
    If the AI does not know the answer to a question, it truthfully says it does not know.

    Current Conversation:
    {chat_history}
    Human: {human_input}
    AI Assistant:
"""

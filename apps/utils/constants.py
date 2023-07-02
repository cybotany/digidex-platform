ACTIVITY_STATUS = [
    ('register', 'Registered'),
    ('update', 'Updated'),
    ('delete', 'Deleted'),
]

ACTIVITY_TYPE = [
    ('plant', 'Plant'),
    ('label grouping', 'Label Grouping'),
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
    ('Aquaponics', 'Aquaponics'),
]

GROWING_MEDIUMS = [
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

GROWING_METHOD_MEDIUM_MAP = {
    'Traditional': ['Soil'],
    'Hydroponics': ['Coco Coir', 'Rockwool', 'Clay Pellets', 'Perlite', 'Vermiculite'],
    'Aquaponics': ['Coco Coir', 'Clay Pellets', 'Perlite', 'Vermiculite'],
}

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

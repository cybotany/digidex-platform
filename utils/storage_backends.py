from storages.backends.s3boto3 import S3Boto3Storage


class AvatarStorage(S3Boto3Storage):
    location = 'media/avatars'
    default_acl = 'public-read'
    file_overwrite = False


class PlantSnapshotStorage(S3Boto3Storage):
    location = 'media/plant_snapshots'
    default_acl = 'public-read'
    file_overwrite = False


class GrowthChamberStorage(S3Boto3Storage):
    location = 'media/growth_chamber_images'
    default_acl = 'public-read'
    file_overwrite = False


class GardenStorage(S3Boto3Storage):
    location = 'media/garden_images'
    default_acl = 'public-read'
    file_overwrite = False

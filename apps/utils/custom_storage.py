from storages.backends.s3boto3 import S3Boto3Storage


class UserSpecificS3Boto3Storage(S3Boto3Storage):
    '''
    Base class to handle the user subdirectory
    '''
    def __init__(self, user_directory_path, *args, **kwargs):
        self.user_directory_path = user_directory_path
        super().__init__(*args, **kwargs)

    def get_available_name(self, name, max_length=None):
        if self.user_directory_path:
            name = "/".join([str(self.user_directory_path), name])
        return super().get_available_name(name, max_length=max_length)


class AvatarStorage(UserSpecificS3Boto3Storage):
    location = 'media/avatars'
    default_acl = 'public-read'
    file_overwrite = False


class JournalImageStorage(UserSpecificS3Boto3Storage):
    location = 'media/journal-images'
    default_acl = 'public-read'
    file_overwrite = False

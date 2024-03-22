from django.db import models

class BaseBooleanField(models.BooleanField):
    pass

class BaseCharField(models.CharField):
    pass

class BaseDateTimeField(models.DateTimeField):
    pass

class BaseEmailField(models.EmailField):
    pass

class BaseForeignKey(models.ForeignKey):
    pass

class BaseManyToManyField(models.ManyToManyField):
    pass

class BaseURLField(models.URLField):
    pass

class BaseUUIDField(models.UUIDField):
    pass

class BaseSlugField(models.SlugField):
    pass

class BaseOneToOneField(models.OneToOneField):
    pass

class BaseImageField(models.ImageField):
    pass

class BaseTextField(models.TextField):
    pass

class BaseIntegerField(models.IntegerField):
    pass

class BaseFloatField(models.FloatField):
    pass

class BaseDecimalField(models.DecimalField):
    pass

class BasePositiveIntegerField(models.PositiveIntegerField):
    pass

class BasePositiveSmallIntegerField(models.PositiveSmallIntegerField):
    pass

class BaseBigIntegerField(models.BigIntegerField):
    pass

class BaseSmallIntegerField(models.SmallIntegerField):
    pass

class BaseAutoField(models.AutoField):
    pass

class BaseBigAutoField(models.BigAutoField):
    pass

class BaseSmallAutoField(models.SmallAutoField):
    pass

class BaseBinaryField(models.BinaryField):
    pass

class BaseDurationField(models.DurationField):
    pass

class BaseGenericIPAddressField(models.GenericIPAddressField):
    pass

class BaseIPAddressField(models.IPAddressField):
    pass

import uuid
from django.db import models
from .enums import GenderTypes


# Create your models here.
class BaseModel(models.Model):
    occupation = models.CharField(max_length=100, blank=True, null=True, default=None)
    gender = models.IntegerField(
        choices=[(gender.value,(gender.name)) for gender in GenderTypes],
        default=GenderTypes.NOT_SET.value
    )
    alias = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)
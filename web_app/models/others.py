import uuid
from django.db import models
from django.utils import timezone
from django.db.models.expressions import Func


class CreatedAtField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAtField(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class IsActive(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ModelUUIDField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __getattribute__(self, __name: str):
        value = super().__getattribute__(__name)
        if isinstance(value, uuid.UUID):
            return value.__str__()
        return value

    class Meta:
        abstract = True


class CreatedAndUpdatedModelFields(CreatedAtField, UpdatedAtField):
    
    class Meta:
        abstract = True


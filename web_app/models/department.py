from django.db import models
from web_app.models.others import *
from web_app.models.regex import *

class Department(ModelUUIDField, CreatedAndUpdatedModelFields,IsActive):
    name = models.CharField(max_length=255, validators=[name])
    description = models.CharField(max_length=350, blank=True, null=True, validators=[description])
    department_under = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def natural_key(self) -> str:
        return self.__str__()
    
from django.db import models
from web_app.models.department import Department
from web_app.models.menus import Menus
from web_app.models.others import *


class Role(ModelUUIDField, CreatedAndUpdatedModelFields, IsActive):
    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField(default=1)
    menu_ids = models.ManyToManyField(Menus, blank=True, null=True)
    is_hod_right = models.BooleanField(default=False,blank=True,null=True)
    is_hidden = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name




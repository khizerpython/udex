from django.db import models

from web_app.models.others import *
from web_app.models.regex import url_name_regex


class Menus(ModelUUIDField, CreatedAndUpdatedModelFields, IsActive):
    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField(default=1)        
    url = models.CharField(max_length=255, validators=[url_name_regex])
    parent_id = models.ForeignKey(to="self", on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)s_parent_id')
    inner_menu_of = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)s_inner_menu_of')

    def __str__(self) -> str:
        return self.name



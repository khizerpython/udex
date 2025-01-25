# Internal Imports
from web_app.models.others import *
from web_app.models.regex import *

class Designation(ModelUUIDField, CreatedAndUpdatedModelFields, IsActive):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=350, blank=True, null=True, validators=[description])
    department_id = models.ForeignKey('web_app.Department', on_delete=models.SET_NULL, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


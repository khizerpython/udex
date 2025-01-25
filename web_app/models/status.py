from django.db import models
from web_app.models.others import *

class Status(ModelUUIDField, CreatedAndUpdatedModelFields):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=300,blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
    def natural_key(self) -> str:
        return self.__str__()

    def natural_key(self) -> str:
        return self.__str__()    

    
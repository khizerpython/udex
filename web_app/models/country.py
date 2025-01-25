from django.db import models
from web_app.models.others import *


class Country(ModelUUIDField, CreatedAndUpdatedModelFields):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class City(ModelUUIDField, CreatedAndUpdatedModelFields):
    name = models.CharField(max_length=255, unique=True)
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

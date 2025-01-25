from django.db import models

from web_app.models.auth import UserForeignKey
from web_app.models.others import *

class FailedLogin(ModelUUIDField, CreatedAndUpdatedModelFields, UserForeignKey):
    failed_login_dateime = models.DateTimeField(auto_now_add=True)
    failed_login_ip_address = models.GenericIPAddressField()

    def __str__(self) -> str:
        return self.failed_login_ip_address
   
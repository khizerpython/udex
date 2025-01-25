from django.db import models

from web_app.models.others import CreatedAndUpdatedModelFields, ModelUUIDField
from web_app.models.auth import UserForeignKey


class FailedResetPasswordAttempt(ModelUUIDField, UserForeignKey, CreatedAndUpdatedModelFields):

    failed_login_ip_address = models.GenericIPAddressField()
    generated_url = models.CharField(max_length=255)    

    def __str__(self) -> str:
        return self.user_id.username




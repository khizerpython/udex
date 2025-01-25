from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model

from web_app import constants
from web_app.utils import global_methods

import os

USER_MODEL = get_user_model()


class CustomSetPasswordAndActivateForm(SetPasswordForm):
    
    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        self.user.is_active = True
        self.user.is_lock = False

        if commit:
            self.user.save()
         
        return self.user


class GenerateUserActivationLinkAgainForm(forms.Form):
    inst_id = forms.ModelChoiceField(queryset=USER_MODEL.objects.exclude(is_active=False, is_lock=False))


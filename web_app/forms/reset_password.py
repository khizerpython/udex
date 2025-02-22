from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import PasswordResetForm, UsernameField, SetPasswordForm
from django.contrib.auth import  get_user_model
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone
from django.forms.utils import ErrorList
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from web_app.utils import global_methods 
from web_app.models import FailedResetPasswordAttempt
from web_app import constants

import os

UserModel = get_user_model()
RESET_PASSWORD_ATTEMPTS_ALLOWED = int(os.getenv("RESET_PASSWORD_ATTEMPTS_ALLOWED", 0))


class CustomResetPasswordForm(PasswordResetForm):

    def __init__(self, data=None, files=None, auto_id="id_%s", prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None, request=None) -> None:
        self.request = request # Inheriting to use the request passed from view class obj while sending email to fetch the user ip to store it in the events.
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order, use_required_attribute, renderer)
    
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True}),
        min_length=3,
        max_length=25,
        validators=[
            RegexValidator(
                constants.USERNAME_REGEX,
                message="Invalid request! doesn't meet the requirements of username"
            )
        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        email:str = cleaned_data.get("email", None)
        username:str = cleaned_data.get("username", None)

        try:
            user_obj = UserModel.objects.get(**{"username": username, "email": email})
        except UserModel.DoesNotExist:
            raise forms.ValidationError("User with given email or username doesn't exists")
        
        # Delete Case handling
        if not user_obj.is_lock and not user_obj.is_active:
            raise forms.ValidationError("User with following details has been deleted. Please contact Infosec Depart for further queries.")

        if user_obj.is_lock:
            raise forms.ValidationError("User with given email and username is locked. Please contact Infosec Depart for further queries.")
        elif not user_obj.is_active:
            raise forms.ValidationError("User with given email and username is inactive. Please contact Infosec Depart for further queries.")
        
        current_reset_password_attempts_of_user = FailedResetPasswordAttempt.objects.filter(user_id = user_obj).count()

        if current_reset_password_attempts_of_user >= RESET_PASSWORD_ATTEMPTS_ALLOWED:
            raise forms.ValidationError("You've reached the limit of reset password. You cannot perform this operation further. For further assistance please contact Infosec Depart.")
        user_obj.last_login = timezone.now()
        user_obj.save()
        self._user_obj = user_obj
        return cleaned_data
    
    def get_users(self, username):
        return UserModel.objects.filter(username=username, is_active=True)

    def send_mail( self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        username = self.cleaned_data["username"]
        client_ip = global_methods.get_client_ip(self.request)
        base_url = context.get("protocol", "")+"://"+context.get("site_name", "")
        reset_password_url = base_url + reverse("password_reset_confirm", kwargs={"uidb64":context.get("uid"), "token":context.get("token") })
        email_message = f"""
          Dear <strong>{username}</strong>, 
          <br>
          <br>
          This email was generated against reset password activity performed against your account in BPM Portal.
          <br>
          <center>
            <a href='{reset_password_url}' style="background-color:#c80000;
              border-radius:4px;
              color:#ffffff;
              display:inline-block;
              font-family: 'Oswald', sans-serif;
              font-size:16px;
              font-weight:bold;
              line-height:50px;
              text-align:center;
              text-decoration:none;
              width:250px;
              -webkit-text-size-adjust:none;">
              Reset Account Password
            </a>
          </center>
          <br>
          If you encounter any problems during Reset Account Password process, Please contact Information Security Team of RapidCompute.
          <br>
          <br>
          <br>
          <b>Best regards</b>,
          <br>
          Information Security
        """
        is_email_send = global_methods.send_generic_email("Reset Account Password - BPM", to_email, {"page_title": "Reset Account Password", "notification_title": "Reset Account Password", "msg": email_message,})
        event_kwargs: dict = {
            "description": f"Reset password link has been sent successfully on {to_email}" if is_email_send == 1 else f"Reset password link has not been sent successfully on {to_email}",
            "page_name": os.path.basename(__file__),
            "line_number": 0,
            "user_ip": client_ip,
            "status_id": constants.SUCCESS if is_email_send == 1 else constants.FAILURE, 
            "event_type_id": constants.INSERT_EVENT if is_email_send == 1 else constants.FAILURE_EVENT,
            "user_id": self._user_obj            
        }
        if is_email_send == 1:
            FailedResetPasswordAttempt.objects.create(failed_login_ip_address=client_ip, generated_url=reset_password_url, user_id=self._user_obj)
            global_methods.insert_event(**event_kwargs)

    def save(
        self,
        domain_override=None,
        subject_template_name="registration/password_reset_subject.txt",
        email_template_name="registration/password_reset_email.html",
        use_https=False,
        token_generator=default_token_generator,
        from_email=None,
        request=None,
        html_email_template_name=None,
        extra_email_context=None,
    ):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data["email"]
        username = self.cleaned_data["username"]
        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override
        email_field_name = UserModel.get_email_field_name()
        for user in self.get_users(username):
            user_email = getattr(user, email_field_name)
            context = {
                "email": user_email,
                "domain": domain,
                "site_name": site_name,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": token_generator.make_token(user),
                "protocol": "https" if use_https else "http",
                **(extra_email_context or {}),
            }
            self.send_mail(
                subject_template_name,
                email_template_name,
                context,
                from_email,
                user_email,
                html_email_template_name=html_email_template_name,
            )

class CustomSetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        min_length=6,
        max_length=50,
        help_text=password_validation.password_validators_help_text_html(),
        validators=[
            RegexValidator(
                constants.PASSWORD_REGEX,
                message="Invalid request! doesn't meet the requirements of password",
            )
        ]
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        min_length=6,
        max_length=50,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        validators=[
            RegexValidator(
                constants.PASSWORD_REGEX,
                message="Invalid request! doesn't meet the requirements of password",
            )
        ]
    )
    
    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        event_kwargs: dict = {
            "description": f"Password of user `{self.user.username}` has been reset successfully" if commit else f"Password of user `{self.user.username}` has not been reset successfully",
            "page_name": os.path.basename(__file__),
            "line_number": 0,
            "user_ip": "0.0.0.0",
            "status_id": constants.SUCCESS if commit else constants.FAILURE, 
            "event_type_id": constants.INSERT_EVENT if commit else constants.FAILURE_EVENT,
            "user_id": self.user            
        }
        if commit:
            self.user.save()
            FailedResetPasswordAttempt.objects.filter(user_id=self.user).delete()
        
        global_methods.insert_event(**event_kwargs)    
        return self.user

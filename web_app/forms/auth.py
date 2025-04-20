from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

from web_app.constants import USERNAME_REGEX, PASSWORD_REGEX
from web_app.models import FailedLogin
from web_app.models import AuthUser
from web_app.models import regex


class CustomAuthenticationForm(AuthenticationForm):

    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True}),
        min_length=3,
        max_length=25,
        validators=[
            RegexValidator(
                USERNAME_REGEX,
                message="Invalid request! doesn't meet the requirements of username",
            )
        ]
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        min_length=6,
        max_length=50,
        validators=[
            RegexValidator(
                PASSWORD_REGEX,
                message="Invalid request! doesn't meet the requirements of password",
            )
        ]
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This user has been set to in-active from portal. Please contact Infosec Depart for further query"),
        "locked": _("This user has been locked from portal. Please contact Infosec Depart for further query"),
        "role_inactive": _("The role assigned to you is not active right now. Please contact Infosec Depart for further query"),
        "role_not_assigned": _("Admin has not assigned any role against your User. Please contact Infosec Depart for further query"),
    }
   
    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This behavior is to
        allow login only active users, and reject login by inactive and locked users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        try:
            if not user.role_id.is_active:
                raise ValidationError(
                    self.error_messages["role_inactive"],
                    code="role_inactive",
                )
        except AttributeError:
            raise ValidationError(
                    self.error_messages["role_not_assigned"],
                    code="role_not_assigned",
                )
        if user.is_lock:
            raise ValidationError(
                self.error_messages["locked"],
                code="locked",
            )
        elif not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )
        
        FailedLogin.objects.filter(user_id=user).delete() # Delete failed login attempts on successfull login


class CreateAuthUserForm(forms.ModelForm):
    first_name = forms.CharField(min_length=3, max_length=30, validators=[regex.first_name_regex])
    last_name = forms.CharField(min_length=3, max_length=30, validators=[regex.last_name_regex])
    username = forms.CharField(min_length=3, max_length=25, validators=[regex.username_regex])
    contact_number = forms.CharField(min_length=10,max_length=13,validators=[regex.contact_number_regex])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_id'].required = True
        self.fields['designation_id'].required = True
        self.fields['city_id'].required = True
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'contact_number', 'dob', 'department_id', 'role_id', 'designation_id', 'city_id',)
        # fields = ('first_name', 'last_name', 'username', 'email', 'contact_number', 'dob', 'department_id', 'role_id', 'designation_id', 'city_id','original_role_id',)


class UpdateAuthUserForm(forms.ModelForm):
    contact_number = forms.CharField(min_length=10,max_length=13,validators=[regex.contact_number_regex])
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'contact_number','email', 'dob', 'department_id', 'role_id', 'designation_id', 'city_id','is_lock',)
        # fields = ('first_name', 'last_name', 'contact_number','email', 'dob', 'department_id', 'role_id', 'designation_id', 'city_id','is_lock','original_role_id',)


class DeleteAuthUserForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('is_active',)

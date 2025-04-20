from django import forms
from django.core import validators

# from web_app.models import Role
from web_app import constants


RIGHTS_CATEGORY_DICT = {
    'HOD':'true',
    'NOT-HOD' : 'false',
}

RIGHTS_AUTHENTICATION_FRONTEND  =  ['true','false']


class RoleForm(forms.ModelForm):

    name = forms.CharField(min_length=3, max_length=30, validators=[validators.RegexValidator(regex=constants.NAME_REGEX)])
    order = forms.IntegerField(min_value=0, max_value=100)

    class Meta:
        model = Role
        fields = ("name", "order", "menu_ids",'is_hod_right')


class UpdateRoleForm(forms.ModelForm):

    name = forms.CharField(min_length=3, max_length=30, validators=[validators.RegexValidator(regex=constants.NAME_REGEX)])
    order = forms.IntegerField(min_value=0, max_value=100)
    
    class Meta:
        model = Role
        fields = ("name", "order", "menu_ids", "is_active","is_hod_right")

        
        
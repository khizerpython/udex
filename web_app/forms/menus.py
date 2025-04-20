from django import forms

# App Level Imports
from web_app.models import Menus
from web_app.models import regex

class CreateMenusForm(forms.ModelForm):

    name = forms.CharField(min_length=3, max_length=30, validators=[regex.role_name])
    url = forms.CharField(min_length=1, max_length=255, validators=[regex.url_name_regex])
    
    class Meta:
        model = Menus
        fields = ('name', 'url','order','parent_id','inner_menu_of')
       


class UpdateMenusForm(forms.ModelForm):

    name = forms.CharField(min_length=3, max_length=30, validators=[regex.role_name])
    url = forms.CharField(min_length=1, max_length=255, validators=[regex.url_name_regex])
    
    class Meta:
        model = Menus
        fields = ("name", "url", "order","is_active", "parent_id","inner_menu_of")       




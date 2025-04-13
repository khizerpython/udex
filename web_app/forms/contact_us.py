from django import forms

# App Level Imports
from web_app.models import Menus
from web_app.models import regex

class ContactUsForm(forms.Form):
    name = forms.CharField(required=True)
    contact = forms.CharField(required=True)
    reason = forms.CharField(required=True)
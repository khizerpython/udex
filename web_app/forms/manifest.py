from django import forms


class GetManifestForm(forms.Form):

    from_date = forms.DateField(required=True)
    to_date = forms.DateField(required=True)


class AirwayBillManifestCheckedForm(forms.Form):

    id = forms.CharField(required=True)
    

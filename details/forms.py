from django import forms


GENDER = (
    'PLEASE SELECT',
    'MALE',
    "FEMALE",

)

# TODO:To add birthday field to the form


class DetailsForm(forms.Form):
    first_name = forms.CharField()
    second_name = forms.CharField()
    email = forms.CharField(widget=forms.TextInput())
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'start with the code'}))
    gender = forms.ChoiceField(choices=GENDER)
    password = forms.CharField(widget=forms.PasswordInput())

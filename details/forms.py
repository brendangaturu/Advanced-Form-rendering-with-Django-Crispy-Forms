from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Column, Layout, Submit

COUNTIES = (
    ('', 'Select County'),
    ('', 'Nairobi'),
    ('', 'Mombasa'),
    ('', 'Kiambu'),
    
)


class AddressForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    second_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Second Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Ngara, Nairobi'})

    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, Studio, or Floor'})
    )
    city = forms.CharField()
    county = forms.ChoiceField(choices=COUNTIES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('second_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'username',
            'password',
            Row(
                Column('address_1', css_class='form-group col-md-6 mb-0'),
                Column('address_2', css_class='form-group col-md-6 mb-0'),

            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('county', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )


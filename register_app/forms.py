from django import forms

class CreateNewUser(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    password = forms.CharField(label="Password", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="First Name", max_length=100, required=False)
    last_name = forms.CharField(label="Last Name", max_length=100, required=False)

from django import forms
from .models import Customer

class CustomerForm(forms.Form):
    lastName = forms.CharField(label="lastName", max_length=100)
    firstName = forms.CharField(label="firstName", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=255)
    phoneNumber = forms.CharField(label="phoneNumber", max_length=15)
    address = forms.CharField(label="address", max_length=255)
    age = forms.IntegerField(label="age")
    gender = forms.ChoiceField(
        label="gender",
        choices=[("Male", "Nam"), ("Female", "Nữ"), ("Other", "Khác")]
    )

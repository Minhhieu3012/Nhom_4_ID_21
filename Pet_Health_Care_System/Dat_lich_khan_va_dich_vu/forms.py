from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customers

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

    class Meta:
        model = Customers
        fields = ["email", "phone", "password1", "password2"]

class CustomerLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ["email", "phone"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control", "readonly": "readonly"}),  # Email không thể chỉnh sửa
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }

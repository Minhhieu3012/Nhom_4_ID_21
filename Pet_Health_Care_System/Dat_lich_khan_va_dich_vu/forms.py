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

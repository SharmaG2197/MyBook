from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Account

class SignupForm(UserCreationForm):
  termsandconditions_and_privacy_policy = forms.BooleanField(required=True, label="I agree to the Terms and Privacy Policy")
  marketing_mail = forms.BooleanField(required=False, label="Receive marketing emails")

  class Meta:
    model = Account
    fields = ('email', 'password1', 'password2', 'termsandconditions_and_privacy_policy', 'marketing_mail')

  def clean(self):
    cleaned_data = super().clean()
    password1 = cleaned_data.get("password1")
    password2 = cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
      self.add_error('password2', "Passwords do not match")
    return cleaned_data


class LoginForm(AuthenticationForm):
  username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'autofocus': True}))



# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\accounts\forms.py

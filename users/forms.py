from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from users.models import User_profile


class EditProfileForm(ModelForm):
    class Meta:
        model = User_profile
        fields = (
                 'email',
                 'first_name',
                 'last_name'
                )
                
class ProfileForm(ModelForm):
    class Meta:
        model = User_profile
        fields = ['email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

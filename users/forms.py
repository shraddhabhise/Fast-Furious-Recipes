from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# code reference: https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8
class UserRegisterForm(UserCreationForm):
    '''
    Class for user registration form
    This form is created using django.contrib.auth.forms of django
    username, email, password is maintained/stored after user registers
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    '''
    class for user update form
    can update username and email fields of user
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    '''
    class for profile update of user
    can update profile picture of user
    '''
    class Meta:
        model = Profile
        fields = ['image']
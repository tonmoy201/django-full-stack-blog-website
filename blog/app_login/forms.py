from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from app_login.models import NewUser


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2',)

class EditProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password')

class NewUserForm(forms.ModelForm):
    class Meta:
        model=NewUser
        fields=('profile_picture',)



from django import forms

from app.models import *


class User_Form(forms.ModelForm):
    class Meta():
        model=User
        fields=['username', 'email', 'password']
        widgets={'password':forms.PasswordInput}

class Profile_Form(forms.ModelForm):
    class Meta():
        model=Profile
        fields=['Address', 'Profile_Pic']
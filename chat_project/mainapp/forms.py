# for logins,signups authentications
from attr import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#user database model

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

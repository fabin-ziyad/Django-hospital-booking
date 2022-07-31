from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

from .models import Contact 
 
 
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2']

class SubscribeForm(forms.Form):
    email = forms.EmailField(required=False)
   

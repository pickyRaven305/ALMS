from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms 
from .models import User_profile
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):    
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name =forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    city  = forms.CharField()
    state  = forms.CharField()
    zipcode =forms.CharField()  
    class Meta:
        model = User
        fields = ["email","first_name","last_name","email","phone","password1","password2","address","city","state","zipcode"]
        
        
class ProfileForm(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name =forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    city  = forms.CharField()
    state  = forms.CharField()
    zipcode =forms.CharField()  
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',"phone","address","city","state","zipcode")
        
class UserPasswordChangeForm(PasswordChangeForm):
    old_password=None
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    
    class Meta :
        model=User
        fields = ("passowrd1", "password2")
        
class UpdateEmailForm(forms.Form):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email')

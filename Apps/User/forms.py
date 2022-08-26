from http.client import FORBIDDEN
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from Apps.User.models import User_profile

class User_registration_form(UserCreationForm):
#    username= forms.CharField(label='Usuario  ',required=True)
    email = forms.EmailField(label='Email  ',required=True)
    password1 = forms.CharField(label='Password  ', widget=forms.PasswordInput,)
    password2 = forms.CharField(label='Password confirmation  ', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k:'' for k in fields} # Saca los comentarios de ayuda


class UserEditForm(UserChangeForm):
    password=forms.CharField(
        help_text="",
        widget=forms.HiddenInput(),
        required=False,
      )
    email = forms.EmailField(label='Email  ',required=True)
    password1 = forms.CharField(label='Password  ', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation  ', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username",'email', 'password1')
        help_texts = {k:'' for k in fields}


class UserEditPerfilForm(UserChangeForm):    
    # # username= forms.CharField(label='Usuario  ',required=True)
    password=forms.CharField(
        help_text="",
        widget=forms.HiddenInput(),
        required=False,
      )
    
    class Meta:
        model = User_profile
        fields = ['first_name','last_name','phone','direccion','description']
        help_texts = {k:'' for k in fields}

    
    
class User_profile_Form(ModelForm):

    class Meta:
        model = User_profile
        fields = ['first_name','last_name','phone','direccion','description','image']

        help_texts = {k:'' for k in fields}
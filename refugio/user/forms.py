from tokenize import group
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class CreateUserForm(UserCreationForm):

    
    #email = forms.EmailField()
    Imagen = forms.ImageField(label='Foto Perfil',required=False)


    class Meta:
        model = User
        fields = ['first_name', 'last_name','username',  'email', 'password1',
                  'password2','Imagen' ]

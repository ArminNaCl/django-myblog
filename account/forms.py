from django import forms
from django.core.exceptions import ValidationError
from .models import User
from django.utils.translation import ugettext_lazy as _
class UserRegistrationForm (forms.ModelForm):
    class Meta:
        model =  User
        fields = {'email', 'full_name' , 'password'}
        labels= {'email': _("Email"), 'full_name': _("Name"), 'password': _("Password")}
        help_texts = {
                    'email': _("Enter your Email"),
                    'full_name': _("Enter your name")
        }
        widgets={
            'email' : forms.TextInput(attrs={'class':"form-control"}),
            'password' : forms.PasswordInput(attrs={'class':"form-control"}),
            'full_name' : forms.TextInput(attrs={'class':"form-control"}),
        }
        
class UserLoginForm(forms.Form):
        email = forms.EmailField(max_length=60 )
        password = forms.CharField( max_length=60 )   


from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from django.contrib.auth.models import User




class CreateUserForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
        widgets = {
        'username' : forms.TextInput(attrs={'class': 'form-control'}),
        'email' : forms.EmailInput(attrs={'class': 'form-control'}),
        'password' : forms.PasswordInput(attrs={'class': 'form-control' ,}),
       }
    


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
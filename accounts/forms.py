from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUserModel
from django.contrib.auth.models import User



class UserRegisterationForm(forms.ModelForm):
    password = forms.CharField( label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'}))    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
        widgets = {
        'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
        'last_name' : forms.TextInput(attrs={'class': 'form-control' ,}),
        'email' : forms.TextInput(attrs={'class': 'form-control'}),
       }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    



class CustomUserForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea())
    national_code = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    phone_number = forms.IntegerField(required=True)
    
    class Meta:
        model = CustomUserModel
        fields = ('phone_number', 'address', 'age', 'gender', 'national_code')
    
    